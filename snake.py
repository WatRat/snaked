import random
import time
import os
import keyboard


class Snake:
    def __init__(self, frame_x, frame_y, snake_len, move_dir, speed):
        self.snake_xy = []
        self.snake_len = snake_len
        self.snake_pos_x = 5
        self.snake_pos_y = 5
        self.move_dir = move_dir
        self.snake_len = snake_len
        self.speed = speed
        self.fruit_pos_x = 0
        self.fruit_pos_y = 0
        self.frame_x = frame_x
        self.frame_y = frame_y
        self.game = True
        self.score = 0

    def get_snake(self):
        if self.move_dir == 'left':
            if self.snake_pos_x > 2:
                self.snake_pos_x -= 1
                self.snake_xy.append([self.snake_pos_x, self.snake_pos_y])

        elif self.move_dir == 'right':
            if self.snake_pos_x < self.frame_x - 2:
                self.snake_pos_x += 1
                self.snake_xy.append([self.snake_pos_x, self.snake_pos_y])

        elif self.move_dir == 'up':
            if self.snake_pos_y > 1:
                self.snake_pos_y -= 1
                self.snake_xy.append([self.snake_pos_x, self.snake_pos_y])

        elif self.move_dir == 'down':
            if self.snake_pos_y < self.frame_y - 2:
                self.snake_pos_y += 1
                self.snake_xy.append([self.snake_pos_x, self.snake_pos_y])

        self.__snake_size_check()

    def __snake_size_check(self):
        if len(self.snake_xy) > self.snake_len:
            self.snake_xy.pop(0)

    def snake_pos(self):
        return self.snake_xy

    def snake_head(self):
        return [self.snake_pos_x, self.snake_pos_y]

    def check_head(self):
        if self.snake_pos_x <= 2 or self.snake_pos_x >= self.frame_x - 2:
            self.stop()
        if self.snake_pos_y <= 1 or self.snake_pos_y >= self.frame_y - 2:
            self.stop()

    def get_new_fruit(self):
        self.fruit_pos_x = random.randint(2, self.frame_x - 2)
        self.fruit_pos_y = random.randint(2, self.frame_y - 2)

    def fruit_pos(self):
        return [self.fruit_pos_x, self.fruit_pos_y]

    def check_eat(self):
        if self.snake_head() == self.fruit_pos():
            self.get_new_fruit()
            self.score += 1

    def get_score(self):
        return self.score

    def stop(self):
        if self.game:
            self.game = False

    def restart(self):
        self.snake_pos_x = 5
        self.snake_pos_y = 5
        self.snake_xy.clear()
        self.get_snake()
        self.move_dir = 't'
        self.get_new_fruit()
        self.score = 0
        self.game = True

    def status(self):
        return self.game

    def wait(self):
        if keyboard.read_key() == "r":
            self.restart()
        elif keyboard.read_key() == "q":
            quit()
        else:
            self.wait()

    def keyboard(self):
        keyboard.on_press_key("w", lambda _: self.__move_up())
        keyboard.on_press_key("s", lambda _: self.__move_down())
        keyboard.on_press_key("a", lambda _: self.__move_left())
        keyboard.on_press_key("d", lambda _: self.__move_right())

    def __move_up(self):
        if not self.move_dir == 'down':
            self.move_dir = 'up'

    def __move_down(self):
        if not self.move_dir == 'up':
            self.move_dir = 'down'

    def __move_left(self):
        if not self.move_dir == 'right':
            self.move_dir = 'left'

    def __move_right(self):
        if not self.move_dir == 'left':
            self.move_dir = 'right'

    def run_console(self, head='@', tail='*'):
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in range(self.frame_y):
            for j in range(self.frame_x):
                if i == 0:
                    print('#', end='')
                elif j == 0:
                    print('#', end='')
                elif j == self.frame_x - 1:
                    print('#', end='')
                elif i == self.frame_y - 1:
                    print('#', end='')
                else:
                    if [j, i] == self.snake_head():
                        print(head, end='')

                    elif [j, i] in self.snake_pos():
                        print(tail, end='')

                    elif [j, i] == self.fruit_pos():
                        print('$', end='')

                    else:
                        print(' ', end='')
                self.check_head()
                self.check_eat()
            print()
        print('score: ', self.get_score())
        self.get_snake()
        time.sleep(self.speed)
