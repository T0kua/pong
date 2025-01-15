import os
import time
import function
from pynput import keyboard

size = (80,15)
player = 5 # p1x = 2 p2.x = size[0] -2
playerSize = 2 # size = 1 + (pSize * 2)
reward = 0
Debug = function.get("debug")
cc = 0
file = open("json.txt","r")
OS = function.get("OS")

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


p = point(10,10)


def Draw(p : point, Debug="False") -> None:
    os.system(OS)
    global reward
    for m in range(size[1]):
        print("|", end="")
        for n in range(size[0]):
            if p.y == m and p.x == n:
                print("0", end="")
            elif (player - playerSize <= m <= player + playerSize) and (n == 2 or n == size[0] - 2):
                print("#",end="")
            else:
                print(" ", end="")
        print("|", end="")
        if m == size[1] // 2 and Debug == "True" :
            print(f"VECTOR [{p.vector[0]}, {p.vector[1]} ]\tPOS - [x:{p.x}, y:{p.y}]", end="")
        if (m - 1 == (size[1]) // 2):
            print(f"SPACE {"0" * (len(str(reward)) -1)}{reward}",end="")
        if (m - 2 == (size[1]) // 2) and Debug == "True":
            print(f"PLAYER {player} CC {cc  }")
        print("\n")

def game_over() -> None :
     global reward
     print("game over")
     if int(function.get("reward")) < reward:
          author = None
          while (author == None):
               author = input("enter your name:")
          function.set("reward", str(reward))
          function.set("author", author)

     exit()

def Logick(p : point) -> None:
    p.metrix()
    global reward
    if p.x >= size[0] - 1 or p.x == 0 : p.vector[0] = game_over()#- p.vector[0]
    if p.y >= size[1] - 1 or p.y == 0 : p.vector[1] = -p.vector[1]
    if (player - playerSize <= p.y  <= player + playerSize) and (p.x == 2 or p.x == size[0] - 2):
         p.bimp()
         reward += 1

def Control(key):
    global player
    global cc
    try:
         key.char
    except:
         return 0
    if key.char in ['w']:
            if cc > 0 : cc = 0
            cc -= 0.5
    elif key.char in ['s']:
            if cc < 0 : cc = 0
            cc += 0.5
    if player - playerSize < 0:
         player = playerSize
    if player + playerSize > size[1]:
         player = size[1] - playerSize
    player += (abs(cc) // 10) * (-1 if cc < 0 else 1) 
    if abs(cc) > 10:
        cc = 0  
    

while not(OS == "cls" or OS == "clear"):
        OS = int(input("enter your Operation system:\n1 - windows\t2 - *Unix"))
        match OS:
            case 1:
                OS = "cls"
            case 2:
                OS  = "clear"
function.set("OS", OS)
file.close()


while True:
    Logick(p)
    Draw(p, Debug)
    listener = keyboard.Listener(on_release=Control)
    time.sleep(0.2)
    listener.start()
