import os
import random
import time

width=20
height=10
StartSnakePosX=2
SnakePosY=4
head='*'

FruitPosX=random.randint(2, width - 2)
FruitPosY=random.randint(2, height - 2)
print(FruitPosY,FruitPosX)
class Frame:
    def snake():
        pass


    def print_frame(self, width, height):
        os.system('cls' if os.name == 'nt' else 'clear')
        i=0
        j=0
        for i in range(height):
            for j in range(width):
                if i == 0:
                    print('#', end='')
                elif j == 0:
                    print('#', end='')
                elif j == width - 1:
                    print('#', end='')
                elif i == height-1:
                    print('#', end='')
                else:
                    if j==SnakePosX and i==SnakePosY:
                        print('*', end='')
                    elif j==FruitPosX and i==FruitPosY:
                        print('$', end='')
                    else:
                        print(' ', end='')
            print()

class Game:
    def move(self):
        global StartSnakePosX, SnakePosX, width, height
        x=0
        SnakePosX=StartSnakePosX
        for i in range(3):
            frame=Frame()
            frame.print_frame(width,height)
            SnakePosX+=1
            time.sleep(.5)

game=Game()
game.move()
