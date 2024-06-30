import API
import heapq
import time
from Direction import Direction  
from Maze import Maze  
from Mouse import Mouse  

class Cell:
    def __init__(self, x, y, cost):
        self.x = x
        self.y = y
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

def dijkstra(maze, start, goal):
    pq = []
    heapq.heappush(pq, Cell(start[0], start[1], 0))
    visited = set()
    parents = {}
    costs = {start: 0}

    while pq:
        cell = heapq.heappop(pq)
        x, y = cell.x, cell.y

        if (x, y) == goal:
            break

        if (x, y) in visited:
            continue
        visited.add((x, y))

        current_cost = costs[(x, y)]

        for direction in Direction:
            nx, ny = getNeighbor((x, y), direction)
            if not maze.contains((nx, ny)) or maze.getWall((x, y), direction) or (nx, ny) in visited:
                continue
            new_cost = current_cost + 1  # Assuming each step has a uniform cost of 1
            if (nx, ny) not in costs or new_cost < costs[(nx, ny)]:
                costs[(nx, ny)] = new_cost
                parents[(nx, ny)] = (x, y)
                heapq.heappush(pq, Cell(nx, ny, new_cost))

    # Reconstruct path from goal to start
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = parents[current]
    path.append(start)
    path.reverse()

    return path

def getNeighbor(current, direction):
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

def getNextCell(maze, mouse):
    current = mouse.getPosition()
    center = (7,8)  # Goal is to reach the maze center

    path = dijkstra(maze, current, center)

    if len(path) > 1:
        return path[1]  # Next cell to move towards
    else:
        return current  # Stay in place if already at center or no valid path found

def main():
    begin = time.time()
    maze = Maze(API.mazeWidth(), API.mazeHeight())  # Initialize maze dimensions using API
    mouse = Mouse(0, 0, Direction.NORTH)  # Initialize mouse at starting position
    start = (0, 0)  # Starting position

    while not maze.inCenter(mouse.getPosition()):
        updateWalls(maze, mouse)
        moveOneCell(maze, mouse)

    end = time.time()
    time.sleep(1)
    API.log(end - begin)

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

def moveOneCell(maze, mouse):
    currentX, currentY = mouse.getPosition()
    next_cell = getNextCell(maze, mouse)
    nextX, nextY = next_cell

    direction = getDirection(currentX, currentY, nextX, nextY)
    current_direction = mouse.getDirection()

    if current_direction.turnLeft() == direction:
        mouse.turnLeft()
    elif current_direction.turnRight() == direction:
        mouse.turnRight()
    elif current_direction != direction:
        mouse.turnAround()

    mouse.moveForward()

def getDirection(currentX, currentY, nextX, nextY):
    if nextX < currentX:
        return Direction.WEST
    elif nextX > currentX:
        return Direction.EAST
    elif nextY < currentY:
        return Direction.SOUTH
    elif nextY > currentY:
        return Direction.NORTH
    else:
        return None  # Should not happen in a valid pathfinding scenario

if __name__ == "__main__":
    main()
