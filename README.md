# IITISoC-24-IVR-3-MICROMOUSE

## GOAL
To develop a maze solving micromouse with hardware integration using simulation

People Involved : 

Mentors:
- [Ampady B R](https://github.com/ampady06)
- [Bhawna Chaudhary](https://github.com/WebWizard104)

Members:
- [Khush Paliwal](https://github.com/KhushPaliwal22)
- [Daksh Chandel](https://github.com/DC-005)
- [Satyajeet Pani](https://github.com/Satyajeet-Pani)

## Initial plan:

1) Algorithm:  To try out and find the best algorithm for our micromouse and simulate it in [mms](https://www.bing.com/ck/a?!&&p=1edceb3b1ea7a884JmltdHM9MTcyMjAzODQwMCZpZ3VpZD0zZmRlMmI3Yi03MDc0LTZlMWMtMzdhNC0zZmIyNzFjNjZmNTgmaW5zaWQ9NTQ0Ng&ptn=3&ver=2&hsh=3&fclid=3fde2b7b-7074-6e1c-37a4-3fb271c66f58&psq=mms+simulator&u=a1aHR0cHM6Ly9naXRodWIuY29tL21hY2tvcm9uZS9tbXM&ntb=1)
2) Hardware: To find the most suitable and optimal hardware for our micromouse according to the requirements and rules.
3) Optimizations: If time allows, to optimize the movement of our mouse.

## Algorithm:

#### Depth-first search:
It involves visiting all the connected nodes of the maze one by one and explores the whole node till it reaches a dead end.

https://github.com/user-attachments/assets/37cedd89-f50f-4885-8b83-93ec46379572

#### Dijkstra's Algorithm:
It is an algorithm for finding the shortest paths between nodes in a weighted graph, which may represent, for example, road networks.

https://github.com/user-attachments/assets/db69f580-81a4-49ad-94b2-37b5b7e51606

#### A* Algorithm:
It is a graph traversal and pathfinding algorithm. A* achieves better performance by using heuristics to guide its search.

https://github.com/user-attachments/assets/170ab3f5-f571-4c94-829b-5c1b3f4d2726

#### Floodfill:
This algorithm calculates the manhattan distances of each cell from the center and makes the mouse move towards the smallest distance from the cell choices it has.
Our mouse doesn't know about the maze wall placements at the starting, so this algorithm dynamically adapts and calculates new distances as soon as the mouse finds a new/undiscovered wall.

https://github.com/user-attachments/assets/f6ae22c9-d815-4f70-b8fa-f30443e4d3fa

We finalised this algorithm for our micromouse as it dynamically adapts to the maze and ensures the shortest path when run for a couple of times.

Next we added return trips to the algorithm as the rules state that the mouse has to return to the start on it's own. This return trip is again utilised by our mouse to find a better path.

https://github.com/user-attachments/assets/c8d6f2ea-c621-45a4-bb10-a4c585f78ac6

##### Algorithm --- Floodfill

## Hardware:
Once we were done with selection of an algorithm, our next step was to look out for the best hardware that we could put in our micromouse.

#### Microcontroller:
The microcontroller is the brain of our mouse. It carries out all the computation, hence we needed a powerful yet compact microcontroller. We compared various microcontrollers on a certain criteria.
![image](https://github.com/user-attachments/assets/eed1e68c-8b9b-4559-8625-ac841faca6b6)

We finalised STM32F103C8T6 for our micromouse.

[![image](https://github.com/user-attachments/assets/3467e8be-3836-4f71-94ee-8dc964868ad5)](https://amzn.in/d/0bSwpOCw)

#### Sensors:
Sensors are the eyes of our mouse. They help the mouse detect where the walls are and move in the center of the maze, without colliding into the wall. After much thought, we went with IR sensors and ultrasonic sensors.
IR sensor:

[![image](https://github.com/user-attachments/assets/d71686f1-1642-4919-a595-22a4281b6984)](https://amzn.in/d/0gtZircN)

Ultrsonic sensor:

[![image](https://github.com/user-attachments/assets/9b5915ac-70ba-4bba-b01c-ef9e3902eaf1)](https://amzn.in/d/07U2rYYQ)

#### Motor:
We needed a high rpm, accurate, and compact motor. A comparison was done keeping in mind these factors.
![image](https://github.com/user-attachments/assets/f17bd96f-cfc7-4691-a189-92631e54c7dd)

We chose N20 metal gear motors since they are powerful and compact.

[![image](https://github.com/user-attachments/assets/33b87dea-ba02-421c-95e2-57e854f07e0f)](https://kitsguru.com/products/n20-12v-micro-metal-gear-motor-1)

#### Motor-Driver:
We needed a motor driver which is accurate and has a voltage range which can drive our motors.
![image](https://github.com/user-attachments/assets/bfe7878a-f8fc-40c2-8e50-5fde1acced8e)

After a detailed comparison, we locked our choice on TB6612FNG Dual H-Bridge motor driver.

[![image](https://github.com/user-attachments/assets/2e4f83a1-453b-4451-b2dd-6ba87834260c)](https://amzn.in/d/0hxGYsam)

#### IMU sensor:
An inertial measurement unit sensor was needed for the bot to know where in the maze it exactly is. Finalised IMU was MPU6050 which is a 6-axis IMU sensor.

[![image](https://github.com/user-attachments/assets/5f13fc47-4a70-4f67-83ba-d1ca8c32a3a1)](https://amzn.in/d/0cyMVpJJ)

#### Power source:
The power source was required to provide power to all the components sufficiently. We first noted down how much power each component took.
We checked the voltage requirement

![image](https://github.com/user-attachments/assets/dffa9964-a1d8-4364-9bb3-0e5d90b00a3a)

and the current requirement

![image](https://github.com/user-attachments/assets/c18767b3-6159-4c85-a0cb-0e1ef537b71b)

After comparing different power sources, we chose two 3.7V lithium ion cell.

[![image](https://github.com/user-attachments/assets/2cbe90ad-7e32-4861-8324-9c65160a946d)](https://amzn.in/d/0if9jwKN)

## Optimizations:
Due to constraints in time and lack of resources, we were unable to optimize much of it performance, but we optimized floodfill to follow more straighter paths.

https://github.com/user-attachments/assets/ca8f1371-aa1d-4062-a40a-bfb3aeb7d7fa

## References:
- https://github.com/mackorone/mms
- https://projects.ieeebruins.com/micromouse/
- https://youtu.be/ktn3C7aXVR0?feature=shared 
- https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/ 
- https://en.wikipedia.org/wiki/Dijkstra's_algorithm 
- https://www.geeksforgeeks.org/flood-fill-algorithm/ 
- https://en.wikipedia.org/wiki/Depth-first_search 
- https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/
- https://github.com/mackorone/breadth-first-search
- https://en.wikipedia.org/wiki/Breadth-first_search 
- https://en.wikipedia.org/wiki/A*_search_algorithm 
- https://www.geeksforgeeks.org/a-search-algorithm/ 
- https://youtu.be/EPDAweXxKJ4?si=ESgo3BmEeuBTNCYC 




