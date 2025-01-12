import time
import os

size = (80,15)

class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.vector = [1,1]
        """
        -1 1   |   1 1
        -1 -1  |    1 -1
        """
    def metrix(self) -> None :
        self.x = self.x + self.vector[0]
        self.y = self.y + self.vector[1]
    def bimp(self):
        self.vector[0], self.vector[1] = - self.vector[0], -self.vector[0]




p = point(10, 10)
try:
    os.system("cls")
    OS = "cls"
except:
    os.system("clear")
    OS = "clear"
def Draw(p : point) -> None:
    os.system(OS)
    for m in range(size[1]):
        print("|", end="")
        for n in range(size[0]):
            if p.y == m and p.x == n:
                print("o", end="")
            else:
                print(" ", end="")
        print("|\n")



def Logick(p : point) -> None:
    p.metrix()
    if p.x == size[0] - 1 or p.x == 0 : p.vector[0] = - p.vector[0]
    if p.y == size[1] - 1 or p.y == 0 : p.vector[1] = -p.vector[1]



while True:
    Logick(p)
    Draw(p)
    time.sleep(0.05)
