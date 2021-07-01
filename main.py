from snake import Snake
# Frame size:
width = 40
height = 10
# Snake settings:
head = '@'
tail = '*'
snake_len = 4
speed = .2
snake_dir = ''

snake = Snake(width, height, snake_len, snake_dir, speed, 1)
snake.get_new_fruit()
snake.get_snake()
snake.keyboard()
while True:
    while snake.status():
        snake.run_console(head, tail)
    print('game over')
    print('press "r" for restart, "q" for quit')
    snake.wait()
