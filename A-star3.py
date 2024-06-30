import API
import collections
import time
import heapq
from Direction import Direction
from Maze import Maze
from Mouse import Mouse
from typing import Tuple, Dict, List

def main():
    begin = time.time()
    maze = Maze(API.mazeWidth(), API.mazeHeight())
    mouse = Mouse(0, 0, Direction.NORTH)
    while not maze.inCenter(mouse.getPosition()):
        updateWalls(maze, mouse)
        moveOneCell(maze, mouse)
    end = time.time()
    time.sleep(1)
    API.log(end - begin)

def updateWalls(maze: Maze, mouse: Mouse):
    position = mouse.getPosition()
    direction = mouse.getDirection()
    if API.wallFront():
        maze.setWall(position, direction)
    if API.wallLeft():
        maze.setWall(position, direction.turnLeft())
    if API.wallRight():
        maze.setWall(position, direction.turnRight())

def moveOneCell(maze: Maze, mouse: Mouse):
    currentX, currentY = mouse.getPosition()
    nextX, nextY = getNextCell(maze, mouse)
    nextDirection = getDirection(currentX, currentY, nextX, nextY)
    currentDirection = mouse.getDirection()

    if currentDirection.turnLeft() == nextDirection:
        mouse.turnLeft()
    elif currentDirection.turnRight() == nextDirection:
        mouse.turnRight()
    elif currentDirection != nextDirection:
        mouse.turnAround()
    mouse.moveForward()

def getDirection(currentX: int, currentY: int, nextX: int, nextY: int) -> Direction:
    if nextX < currentX:
        return Direction.WEST
    elif nextY < currentY:
        return Direction.SOUTH
    elif nextX > currentX:
        return Direction.EAST
    elif nextY > currentY:
        return Direction.NORTH

def getNextCell(maze: Maze, mouse: Mouse) -> Tuple[int, int]:
    initial = mouse.getPosition()
    goal_cells = [(API.mazeWidth() // 2, API.mazeHeight() // 2)]
    if API.mazeWidth() % 2 == 0:
        goal_cells.append((API.mazeWidth() // 2 - 1, API.mazeHeight() // 2))
        goal_cells.append((API.mazeWidth() // 2, API.mazeHeight() // 2 - 1))
        goal_cells.append((API.mazeWidth() // 2 - 1, API.mazeHeight() // 2 - 1))
    open_set = []
    heapq.heappush(open_set, (0, initial))
    came_from: Dict[Tuple[int, int], Tuple[int, int]] = {}
    g_score: Dict[Tuple[int, int], int] = {initial: 0}
    f_score: Dict[Tuple[int, int], int] = {initial: heuristic(initial, goal_cells[0])}

    while open_set:
        _, current = heapq.heappop(open_set)
        
        if maze.inCenter(current):
            return reconstruct_path(came_from, current, initial)

        for direction in Direction:
            neighbor = getNeighbor(current, direction)
            if not maze.contains(neighbor) or maze.getWall(current, direction):
                continue
            
            tentative_g_score = g_score[current] + 1  # assume cost of moving to neighbor is 1

            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score 
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal_cells[0])
                if neighbor not in [i[1] for i in open_set]:
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

def heuristic(cell: Tuple[int, int], goal: Tuple[int, int]) -> int:
    return abs(cell[0] - goal[0]) + abs(cell[1] - goal[1])  # Manhattan distance

def reconstruct_path(came_from: Dict[Tuple[int, int], Tuple[int, int]], current: Tuple[int, int], start: Tuple[int, int]) -> Tuple[int, int]:
    while came_from[current] != start:
        current = came_from[current]
    return current

def getNeighbor(current: Tuple[int, int], direction: Direction) -> Tuple[int, int]:
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

if __name__ == "__main__":
    main()
