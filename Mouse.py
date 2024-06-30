import API

from Direction import Direction


class Mouse:
    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d
        self.streak = 1

    def getPosition(self):
        return (self.x, self.y)

    def getDirection(self):
        return self.d
    
    def getDirectionTo(self,position):
        if position[0] == (self.x)-1:
            return Direction.EAST
        elif position[0] == (self.x)+1:
            return Direction.WEST
        elif position[1] == (self.y)-1:
            return Direction.SOUTH
        elif position[1] == (self.y)+1:
            return Direction.NORTH

    def turnLeft(self):
        API.turnLeft()
        self.d = self.d.turnLeft()

    def turnRight(self):
        API.turnRight()
        self.d = self.d.turnRight()

    def turnAround(self):
        self.turnRight()
        self.turnRight()

    def moveForward(self):
        API.moveForward()
        if self.d == Direction.NORTH:
            self.y += 1
        if self.d == Direction.EAST:
            self.x += 1
        if self.d == Direction.SOUTH:
            self.y -= 1
        if self.d == Direction.WEST:
            self.x -= 1
    
    