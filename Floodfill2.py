import API
import time
from Direction import Direction  
from Maze import Maze  
from Mouse import Mouse  

from collections import deque

def floodFillManhattanDistances(maze, goals):
    width = API.mazeWidth()
    height = API.mazeHeight()
    distances = [[None] * height for _ in range(width)]
    queue = deque([(goal[0], goal[1], 0) for goal in goals])  # Using deque for efficient pop from the front
    for goal in goals:
        distances[goal[0]][goal[1]] = 0

    while queue:
        x, y, dist = queue.popleft()  # pop from the front of the deque
        for direction in Direction:
            if maze.getWall((x, y), direction):
                # if x !=0 and x!=15 and y!=0 and y!=15:
                #     API.log(f'continued at {x},{y} in drin {direction}')
                continue
            else:
                nx, ny = getNeighbor((x, y), direction, maze)
                # API.setText(nx,ny,f'{maze.getWall((x, y), direction)}')
                if maze.contains((nx, ny)) and distances[nx][ny] == None:
                    distances[nx][ny] = dist + 1
                    # API.setText(nx,ny,f'{distances[nx][ny]}')
                    # time.sleep(0.01*distances[nx][ny])
                    queue.append([nx, ny, distances[nx][ny]])

    return distances


def getNeighbor(current, direction, maze):
    x, y = current
    if direction == Direction.NORTH:
        y += 1
    elif direction == Direction.EAST:
        x += 1
    elif direction == Direction.SOUTH:
        y -= 1
    elif direction == Direction.WEST:
        x -= 1
    return (x, y)

def moveTowardsSmallestDistance(maze, mouse, distances, visited):
    current_position = mouse.getPosition()
    current_direction = mouse.getDirection()
    min_distance = float('inf')
    next_direction = None
    next_position = None

    for direction in Direction:
        neighbor = getNeighbor(current_position, direction, maze)
        if maze.contains(neighbor) and not maze.getWall(current_position, direction) and neighbor not in visited and distances[neighbor[0]][neighbor[1]] != None:
            if distances[neighbor[0]][neighbor[1]] < min_distance:
                min_distance = distances[neighbor[0]][neighbor[1]]
                next_direction = direction
                next_position = neighbor
        

    if next_position:
        while current_direction != next_direction:
            if current_direction.turnLeft() == next_direction:
                mouse.turnLeft()
            elif current_direction.turnRight() == next_direction:
                mouse.turnRight()
            else:
                mouse.turnAround()
                # distances = floodFillManhattanDistances(maze, goal_cells)
            current_direction = mouse.getDirection()

        mouse.moveForward()
        current_position = mouse.getPosition()
        visited.add(current_position)  # Update visited set with the new position  
        return True  # Successfully moved

def getDirection(current, target):
    cx, cy = current
    tx, ty = target

    if tx > cx:
        return Direction.EAST
    elif tx < cx:
        return Direction.WEST
    elif ty > cy:
        return Direction.NORTH
    elif ty < cy:
        return Direction.SOUTH
    else:
        return None
def moveToStart(maze):
    width = API.mazeWidth()
    height = API.mazeHeight()
    distances = [[None] * height for _ in range(width)]
    queue = deque([(0, 0, 0)])  # Using deque for efficient pop from the front
    distances[0][0] = 0
    # for x in range(16):
    #     for y in range(16):
    #         API.setText(x,y,f'{distances[x][y]}')
    #         time.sleep(0.005)

    while queue:
        x, y, dist = queue.popleft()  # pop from the front of the deque
        for direction in Direction:
            if maze.getWall((x, y), direction):
                # if x !=0 and x!=15 and y!=0 and y!=15:
                #     API.log(f'continued at {x},{y} in drin {direction}')
                continue
            else:
                nx, ny = getNeighbor((x, y), direction, maze)
                # API.setText(nx,ny,f'{maze.getWall((x, y), direction)}')
                if maze.contains((nx, ny)) and distances[nx][ny] == None:
                    distances[nx][ny] = dist + 1
                    # API.setText(nx,ny,f'{distances[nx][ny]}')
                    # time.sleep(0.005*distances[nx][ny])
                    queue.append([nx, ny, distances[nx][ny]])

    return distances
def main():
    begin = time.time()
    maze = Maze(API.mazeWidth(), API.mazeHeight())  # Initialize maze dimensions using API
    mouse = Mouse(0, 0, Direction.NORTH)  # Initialize mouse at starting position
    start = (0, 0)  # Starting position
    # Define the goal cells (e.g., the center of the maze)
    goal_cells = [(API.mazeWidth() // 2, API.mazeHeight() // 2)]
    if API.mazeWidth() % 2 == 0:
        goal_cells.append((API.mazeWidth() // 2 - 1, API.mazeHeight() // 2))
        goal_cells.append((API.mazeWidth() // 2, API.mazeHeight() // 2 - 1))
        goal_cells.append((API.mazeWidth() // 2 - 1, API.mazeHeight() // 2 - 1))

    # Calculate Manhattan distances using flood fill from the goal cells
    distances = floodFillManhattanDistances(maze, goal_cells)

    visited = set()  # Set to keep track of visited cells
    visited.add(start)  # Mark the starting cell as visited
    for i in range(3):
        while not maze.inCenter(mouse.getPosition()):
            updateWalls(maze, mouse)
            distances = floodFillManhattanDistances(maze, goal_cells)
            # API.log(distances)
            moved = moveTowardsSmallestDistance(maze, mouse, distances, visited)

            if not moved:
                visited = set()
                distances = floodFillManhattanDistances(maze, goal_cells)
                moved = moveTowardsSmallestDistance(maze, mouse, distances, visited)
        if i < 2:
            visited = set()
            while mouse.getPosition() != (0,0):
                updateWalls(maze, mouse)
                distances = moveToStart(maze)
                moved = moveTowardsSmallestDistance(maze, mouse, distances, visited)
                if not moved:
                    visited = set()
                    distances = moveToStart(maze)
                    moved = moveTowardsSmallestDistance(maze, mouse, distances, visited)

    end = time.time()
    time.sleep(1)
    API.log("Maze solved in {:.2f} seconds".format(end - begin))

def updateWalls(maze, mouse):
    position = mouse.getPosition()
    direction = mouse.getDirection()

    # Update walls based on sensor information
    if API.wallFront():
        maze.setWall(position, direction)
    if API.wallLeft():
        maze.setWall(position, direction.turnLeft())
    if API.wallRight():
        maze.setWall(position, direction.turnRight())

if __name__ == "__main__":
    main()
