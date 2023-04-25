import pygame
import sys
import os
import random
import datetime
import psycopg2 as pgsql
import time

os.chdir('D:\Git\PP2\Lab_8\snake')
pygame.init()

print('Connecting to the PostgreSQL database...')
connection=pgsql.connect(host="localhost", dbname="snake", user="postgres", 
                         password="damir2004")


cur = connection.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS Snake 
(
    player VARCHAR(255),
    score INT
);
""")


background = pygame.image.load('D:\Git\PP2\Lab_8\snake\snake.png')

SIZE_BLOCK = 20
WHITE = (255, 255, 255)
FRAME_COLOR = (0, 255, 204)
HEADER_COLOR = (0, 204, 153)
SNAKE_COLOR = (0, 102, 0)
COUNT_BLOCKS = 20
BLUE = (204,255,255)
RED = (224, 0, 0)
MARGIN = 1
HEADER_MARGIN = 70

size = [SIZE_BLOCK*COUNT_BLOCKS+2*SIZE_BLOCK+MARGIN*COUNT_BLOCKS, 
        SIZE_BLOCK*COUNT_BLOCKS+2*SIZE_BLOCK+MARGIN*COUNT_BLOCKS+HEADER_MARGIN]
screen = pygame.display.set_mode(size)
timer = pygame.time.Clock()
courier = pygame.font.SysFont('courier', 36, 1)
courier_small = pygame.font.SysFont('courier', 20, 0, 1)

class SnakeBlock:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def is_inside(self):
        return 0<=self.x<COUNT_BLOCKS and 0<=self.y<COUNT_BLOCKS
    
    def __eq__(self, other):
        return isinstance(other, SnakeBlock) and self.x == other.x and self.y == other.y



def draw_block(color, row, column):
    pygame.draw.rect(screen, color, [SIZE_BLOCK+column*SIZE_BLOCK + MARGIN*(column),
                                              HEADER_MARGIN+SIZE_BLOCK+row*SIZE_BLOCK + MARGIN*(row), 
                                              SIZE_BLOCK, SIZE_BLOCK])

def point_position(row, column):
    size = [SIZE_BLOCK+column*SIZE_BLOCK + MARGIN*(column),
                                              HEADER_MARGIN+SIZE_BLOCK+row*SIZE_BLOCK + MARGIN*(row), 
                                              SIZE_BLOCK, SIZE_BLOCK]
    return size

def start_the_game():

    print([SIZE_BLOCK+10*SIZE_BLOCK + MARGIN*(10),
                                              HEADER_MARGIN+SIZE_BLOCK+10*SIZE_BLOCK + MARGIN*(10), 
                                              SIZE_BLOCK, SIZE_BLOCK])
    def get_random_empty_block():
        x = random.randint(0, COUNT_BLOCKS-1)
        y = random.randint(0, COUNT_BLOCKS-1)
        point = random.randint(1, 5)
        spawn_time = datetime.datetime.now()
        empty_block = SnakeBlock(x, y)
        while empty_block in snake_blocks:
            empty_block.x = random.randint(0, COUNT_BLOCKS-1)
            empty_block.y = random.randint(0, COUNT_BLOCKS-1)
        return empty_block, point, spawn_time


    snake_blocks = [SnakeBlock(9,9), SnakeBlock(9, 10), SnakeBlock(9, 11)]
    apple, point, spawn = get_random_empty_block()

    d_row = 0
    d_col = 1
    total = 0
    speed = 1

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('exit')
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and d_col!=0:
                    d_row = -1
                    d_col = 0
                elif event.key == pygame.K_DOWN and d_col!=0:
                    d_row = 1
                    d_col = 0
                elif event.key == pygame.K_RIGHT and d_row!=0:
                    d_row = 0
                    d_col = 1
                elif event.key == pygame.K_LEFT and d_row!=0:
                    d_row = 0
                    d_col = -1

        screen.fill(FRAME_COLOR)
        pygame.draw.rect(screen, HEADER_COLOR, [0, 0, size[0], HEADER_MARGIN])

        text_total = courier.render(f"Total: {total}", 1, WHITE)
        text_speed = courier.render(f"Speed: {speed}", 1, WHITE)
        point_surface = courier.render(f"{point}", 1, "BLACK")
        screen.blit(text_total, (SIZE_BLOCK, SIZE_BLOCK))
        screen.blit(text_speed, (SIZE_BLOCK+230, SIZE_BLOCK))


        for row in range(COUNT_BLOCKS):
            for column in range(COUNT_BLOCKS):

                if (row+column)%2==0:
                    color = BLUE
                else:
                    color = WHITE 

                draw_block(color, row, column)

        head = snake_blocks[-1]
        if not head.is_inside():
            print('crash')
            cur.execute(f'''
            UPDATE Snake
            SET score = {total}
            WHERE player = '{name}'
            ''')
            connection.commit()
            break
            # pygame.quit()
            # sys.exit()

        draw_block(RED, apple.x, apple.y)
        screen.blit(point_surface, point_position(apple.x, apple.y))
        for block in snake_blocks:
            # x, y = block
            draw_block(SNAKE_COLOR, block.x, block.y)

        now = datetime.datetime.now()
        if (now - spawn).seconds.real >= point + 1:
            apple, point, spawn = get_random_empty_block()

        if apple == head: 
            total += point
            speed = total//3 + 1
            snake_blocks.append(apple)
            apple, point, spawn = get_random_empty_block()
        
        new_head = SnakeBlock(head.x + d_row, head.y + d_col)


        if new_head in snake_blocks:
            print('crash yourself')
            cur.execute(f'''
            UPDATE Snake
            SET score = {total}
            WHERE player = '{name}'
            ''')
            connection.commit()
            break

        snake_blocks.append(new_head)
        snake_blocks.pop(0)

        time = courier_small.render("Time for respawn food: " + str(point+1 -(now - spawn).seconds.real), 1, RED)
        screen.blit(time, (20, 508))

        mkll = courier_small.render("by mkll", 0, "BLACK")
        screen.blit(mkll, (357, 508))
        pygame.display.flip()
        timer.tick(3+speed)
    user()


def user():
    print("Enter your name:\n")
    name=str(input())

    cur.execute(f'''
    SELECT *
    FROM Snake
    WHERE player = '{name}'
    ''')

    if len(cur.fetchall())==0:
        cur.execute(f'''
        INSERT INTO Snake
        VALUES('{name}', 0)
        ''')
    else:
        cur.execute(f'''
        SELECT *
        FROM Snake
        WHERE player = '{name}'
        ''')
        print(f"User's score = {cur.fetchone()[1]}")


    print('Game will start in 5 seconds')
    time.sleep(5)


    start_the_game()

user()