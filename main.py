import os
import random
import time
import keyboard

width = 40
height = 10
StartSnakePosX = 2
StartSnakePosY = 4
head = '*'
tail = '0'
GAME = True

FruitPosX = random.randint(2, width - 2)
FruitPosY = random.randint(2, height - 2)

print(FruitPosY, FruitPosX)
SnakeDir = 't'

keyboard.on_press_key("w", lambda _: game.Up())
keyboard.on_press_key("s", lambda _: game.Down())
keyboard.on_press_key("a", lambda _: game.Left())
keyboard.on_press_key("d", lambda _: game.Right())

class Frame:
    def print_frame(self, width, height, SnakePosX, SnakePosY):
        os.system('cls' if os.name == 'nt' else 'clear')
        i = 0
        j = 0
        for i in range(height):
            for j in range(width):
                if i == 0:
                    print('#', end='')
                elif j == 0:
                    print('#', end='')
                elif j == width - 1:
                    print('#', end='')
                elif i == height - 1:
                    print('#', end='')
                else:
                    if j == SnakePosX and i == SnakePosY:
                        print('*', end='')
                    elif j == FruitPosX and i == FruitPosY:
                        print('$', end='')
                    elif SnakePosX == FruitPosX and SnakePosY == FruitPosY:
                        game.fruit()
                    else:
                        print(' ', end='')
            print()


class Game:
    def start(self):
        global StartSnakePosX, StartSnakePosY, width, height, SnakeDir
        x = 0
        SnakePosX = StartSnakePosX
        SnakePosY = StartSnakePosY
        frame = Frame()
        while GAME == True:

            if SnakeDir == 'l':
                if SnakePosX > 2:
                    SnakePosX-=1

            if SnakeDir == 'r':
                if SnakePosX < width -2:
                    SnakePosX+=1

            if SnakeDir == 'u':
                if SnakePosY > 1:
                    SnakePosY-=1

            if SnakeDir == 'd':
                if SnakePosY < height-2:
                    SnakePosY+=1

            frame.print_frame(width, height,SnakePosX, SnakePosY)
            time.sleep(.2)
    def fruit(self):
        global FruitPosX, FruitPosY
        FruitPosX = random.randint(2, width - 2)
        FruitPosY = random.randint(2, height - 2)

    def Up(self):
        global SnakeDir
        if not SnakeDir == 'd':
            SnakeDir = 'u'

    def Down(self):
        global SnakeDir
        if not SnakeDir == 'u':
            SnakeDir = 'd'

    def Left(self):
        global SnakeDir
        if not SnakeDir == 'r':
            SnakeDir = 'l'


    def Right(self):
        global SnakeDir
        if not SnakeDir == 'l':
            SnakeDir = 'r'



game = Game()
game.start()
