import math

class Point:
    def __init__(self, x=0, y=1):
        self.__x, self.__y = x, y

    def read(self):
        self.__x, self.__y = map(int, input().split())

    def print(self):
        print(f"({self.__x}, {self.__y})")

    def move(self, dx, dy):
        self.__x += dx
        self.__y += dy

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def distance(self, p=None):
        if p is None:
            return math.sqrt(self.__x**2 + self.__y**2)
        else:
            return math.sqrt((p.getX() - self.__x)**2 + (p.getY() - self.__y)**2)
