ENPM 661: Planning for Autonomous Robots
Project - 3 (Part - 1): A-Star Algorithm for Project 2
Akshay Bajaj

Directions to Run the program: 
	- To run the code "python3" and "pygame" must be installed on the PC. 
	- Go inside Python scripts subfolder and double click on "AStar_Grid1.py" file

							OR

	- Just open the command prompt go to the directory where the code is downloaded. 
	- Now type “python AStar_Grid1.py”.
        - The code will start running (wait for the computation to complete).
	- And a window with output will appear along with a text output.


Some information about the code and files: 
	- The code stops when the goal is found or more than 100,000 nodes have been generated.
	- The algorithm makes sure that it does not copy the same nodes in the "Open" or "Closed" list and "FinalTableDict" dictionary.
	- The distance (f, g and total), nodes (selected on the basis of minimum distance) are computed and stored in "FinalTableDict" dictionary.
	- The path is traversed and stored in the lise named "n".

Understanding the Output:
	- Screenshots are stored inside Output Screenshot subfolder for different combinations of start and goal node.
	- In the output, "Black" color shows "obstacle space nodes", "Red" color shows the "final path nodes".
 