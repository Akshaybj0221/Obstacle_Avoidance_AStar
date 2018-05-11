import math
from scipy.special import kn
from scipy.stats import norm
from scipy.stats import poisson
from scipy import optimize
import numpy.matlib
import numpy as np
import random




def sys(k, xkm1, uk, noise, h):
    temp = np.array([math.cos(uk), math.sin(uk)]).reshape(1,2)
    return xkm1+((numpy.dot(v, temp))*h) + noise # (returns column vector)

## PDF of process noise and noise generator function
def p_sys_noise(u, sigma_u):
    return norm.pdf(u, 0, sigma_u)

def gen_sys_noise(sigma_u):
    return np.random.normal(0, sigma_u, 1)        
 
## PDF of observation noise and noise generator function

def p_obs_noise(v, sigma_v):
    return norm.pdf(v, 0, sigma_v)

def gen_obs_noise(sigma):
    return np.random.normal(0, sigma, 1)        

## Transition prior PDF p(x[k] | x[k-1])
# (under the suposition of additive process noise)
def p_xk_given_xkm1(k, xk, xkm1, uk, h):
    return p_sys_noise(xk - sys(k, xkm1, uk, 0, h))

## Observation likelihood PDF p(z[k] | x[k], r)
def p_zk_given_sk(x, l):
    return float(poisson.pmf(x,l))

def calR(lambd, a, Qo, v2, w):
  return float(Qo) / float(  math.log(float(lambd)/float(a))  ) * float(kn  (0, float(numpy.linalg.norm(v2-w)) ) ) / float(lambd)

def systematic_resample(xk, wk, nx, Ns):
   N = len(wk)
  
   # make N subdivisions, and choose positions with a consistent random offset
   positions = (np.random.rand(1) + np.arange(N)) / N 
   indexes = np.zeros(N, 'i')
   cumulative_sum = np.cumsum(wk)
   i = 0
   j = 0
  
   while (i < N):
      if positions[i] < cumulative_sum[j]:
         indexes[i] = j
         i += 1
      else:
         j += 1

   temp3 = np.zeros((nx,Ns))
   for i in indexes:
      temp3[0][i] = xk[0][i]
      temp3[1][i] = xk[1][i]

   xk = temp3                    # extract new particles

   wk = []         # now all particles have the same weight
   for i in range(N):
      wk.append(float(1)/float(N))

   return (xk,wk,indexes)


def pFilter(k, Ns, w, particles, mu, sigma, h, zk, uk,T, x_curr, y_curr):


  
  if (k == 0):
    print("error: k must be an integer greater or equal than 2")

  ## Initialize variables
  nx = len(particles[0])               # number of states
  wkm1 = w[k-1]                     # weights of last iteration
  
  if (k == 1):
    for i in range(Ns):
      temp = []
      xrand = grid_length*np.random.rand(1)
      yrand = grid_length*np.random.rand(1)
      zrand = np.random.lognormal(mu,sigma,1)/5

      xrand = xrand[0]
      yrand = yrand[0]
      zrand = zrand[0]

      particles[0][0][i] = xrand
      particles[0][1][i] = yrand
      particles[0][2][i] = zrand

    for i in range(Ns):
      wkm1[i] = float(1)/float(Ns)

  
  
  ## Separate memory
  xkm1 = particles[k-1] # extract particles from last iteration;
  

  xk = np.zeros((nx,Ns))
  wk = np.zeros((Ns))

 
  for i in range(Ns):
    # Sampling

    xktemp = []
    xktemp.append(xkm1[0][i])
    xktemp.append(xkm1[1][i])

    res = sys(k, np.array(xktemp).reshape(1,2), uk, gen_sys_noise(sigma), h)

    res = res.tolist()


    xk[0][i]=res[0][0]
    xk[1][i]=res[0][1]
    xk[2][i]=xkm1[2][i]

    # Prediction   
    v2 = np.array([x_curr, y_curr]).reshape(1,2)
    w2 = np.array([xk[0][i], xk[1][i]]).reshape(1,2)
    rate_estimate = calR(lambd, a, Qo, v2, w2)
    mu_estimate = rate_estimate*h

 
    #Computing weights
    prob = p_zk_given_sk(zk,mu_estimate);

 
    wkmax = len(wkm1)
    for j in range(wkmax):
      wk[j] = float(wkm1[j])*float(prob) 


   
  ## Normalize weight vector

  sum1 = 0
  i = 0
  while i < len(wk)-1:
    sum1 += wk[i]
    i+=1

  wk = [float(x)/float(sum1) for x in wk]

  # 
  ## Calculate effective sample size: eq 48, Ref 1
  temp2 = []
  for i in wk:
    temp2.append(i**2) 

  sum1 = 0
  for i in temp2:
    sum1 += i
           
  Neff = float(1)/float(sum1)


  ## Resampling
  # Sample on each iteration:
  # Alternative: Bootstrap particle filter
  Nt=Ns/2
  if (Neff < Nt):
    [xk, wk, ind] = systematic_resample(xk, wk, nx, Ns)

  ## Compute estimated state 
  xhk = np.zeros((nx, 1))
  
  for i in range(Ns):
    xhk[0] += wk[i]*xk[0][i]
    xhk[1] += wk[i]*xk[1][i]
    xhk[2] += wk[i]*xk[2][i]


  ## Store new weights and particles

  w[k] = wk
  particles[k] = xk

  #finalPF = []
  temp4 = [k, Ns, wk, xk]
  finalPF.append(temp4)



  return  [xhk, finalPF]

def values():
   return [s,pos_curr,h,v,m,lambd]

#def DFIM(angle):
 # return angle**2


def DFIM(angle, s,pos_curr,h,v,m,lambd):
   #s,pos_curr,h,v,m,lambd = values()
   #print(pos_curr)

   q_array = []
   v2 = np.array(pos_curr).reshape(1,2)
   w = np.array(s).reshape(1,2)

   delta_time = 1
   c=pow(v*delta_time*numpy.linalg.norm(v2-w)*math.sin(angle),2)
   k=1
   while k<=m:
      q_array.append(v2-w)
      v2 = v2 + v*np.array([math.cos(angle), math.sin(angle)]).reshape(1,2)
      k+=1

   res1=0
   i=2
   while i<=m-2:
      temp10 = np.array(q_array[i]).reshape(1,2)
      alpha = pow(kn(1,numpy.linalg.norm(temp10)/lambd),2)/(kn(0,numpy.linalg.norm(temp10))/lambd) 
      beta=alpha/(pow(numpy.linalg.norm(temp10),2))
      res=0
      j=1
      while j<=i-1:
         temp11 = np.array(q_array[i]).reshape(1,2)
         fqj=(pow(kn(1,numpy.linalg.norm(temp11)/lambd),2))/(kn(0,numpy.linalg.norm(temp11))/lambd) 
         res=((fqj*pow(i-j+1,2))/pow(numpy.linalg.norm(temp11),2))+res;
         j+=1
       
      res1=beta*res+res1  
      i+=1    
      
   return math.log(c*res1)



x_curr=49
y_curr=49
grid_width=50
grid_length=50
speed=0.1
angles_past=[0.0]
start = 2;
x_past=[start]
y_past=[start]
for i in range(22):
  start+=2
  x_past.append(start)
  y_past.append(start)

for i in range(23):
  angles_past.append(0.408)

x_past.append(49)
y_past.append(49)
angles_past.append(-0.839)
pos_curr=[x_curr,y_curr]




# Nonlinear Diffusion Model
Qo=1 #Emission rate
D=1 #Isotropic Diffusivity (m/s^2)
a=1 #Sensor size (m)
tau=250 #Average lifetime of particles propogating (s)
h=1 #Sampling time (s)
r=[x_curr,y_curr] #Current position
s=[grid_width/2, grid_length/2] #Source position
v=speed #Constant body speed (m/s)
vc=[0,0] #Wind/current speed (m/s)
m = 10
vc = np.array(vc).reshape(1,2)

#Calculated Parameters
lambd=math.sqrt(D*tau)



## Generate Measurements for Positions

position = [x_past, y_past] #x_past/y_past is a list of all the x values till present

angle_inputs = angles_past

z_measurements = []


i = 0
while(i < len(position[0])): 

    temp = [position[0][i], position[1][i]]
    v2 = np.array(temp).reshape(1,2)
    w = np.array(s).reshape(1,2)
    R = calR(lambd, a, Qo, v2, w)
    mu= R*h


    temp2 = np.random.poisson(mu, 1)
    temp2 = temp2[0]
    z_measurements.append(temp2)


    if (numpy.linalg.norm(v2-w)<=20):
        z_measurements[-1] += 1

    if (numpy.linalg.norm(v2-w)<=5): 
        z_measurements[-1] += 2

    i+=1

#print("z_measurements: ", z_measurements)

## Particle Filter

# Hypotheses
N=10000

# 
## Number of time steps
T = len(position[0])
nx = 3 #Number of states: x (location),y (location) and Qo (emittance rate measurement)
nz = 1 #Number of observations: # number of particles z
# 
## PDF of process noise and noise generator function
nu = 3                                         
sigma_u = math.sqrt(1)

# 
## PDF of observation noise and noise generator function
nv = 1                                           
sigma_v = 1

## Transition prior PDF p(x[k] | x[k-1])
# (under the suposition of additive process noise)

## Initial PDF 
mu=1
sigma=1.2
gen_x0 = grid_length*np.random.rand(1)
gen_y0 = grid_width*np.random.rand(1)
gen_Q0 = np.random.lognormal(mu,sigma,1)/5

## Simulate system
x = position


## Separate memory
xh = []
temp = x[0]
temp.append(z_measurements[0]/h)
xh.append(temp)

zh = []
zh.append(z_measurements[0]) 


## Estimate state
T = len(position) 
Ns = 500
k = 1

arrX = np.zeros((T, Ns))
arr3D = np.zeros((T, nx,Ns))
finalPF = []
finalPF.append([1, Ns, arrX, arr3D])

result = []
while (k<T):
 
  [xhTemp, finalPFTemp] = pFilter(k, finalPF[k-1][1], finalPF[k-1][2], finalPF[k-1][3], mu, sigma, h, z_measurements[k-1], angle_inputs[k-1],T, x_curr, y_curr) #sys, z_measurements[k], finalPF, angle_inputs[k], x[k], h)

  result.append(xhTemp)
  finalPF.append(finalPFTemp)
  k = k+1



source_estimate = []
source_estimate = result[-1]
 
sRes = [source_estimate[0], source_estimate[1]]
print('sRes', sRes)

optimal_angle = optimize.fminbound(DFIM, -3.14, 3.14,  args = (sRes,pos_curr,h,v,m,lambd))

print(optimal_angle)