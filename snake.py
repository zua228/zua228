import random
import pygame
import sys
import time
import multiprocessing


def func():
    score = 0


    class Snake(object):
        def __init__(self):
            self.status = 0
            self.dead = False
            self.direction = 'right'
            self.body_list = [(200, 0), (200, 20), (200, 40), (200, 60)]
            self.step = 20
            self.snake_x = self.body_list[-1][0]
            self.snake_y = self.body_list[-1][1]
            self.snake_head_rect = pygame.Rect(self.snake_x, self.snake_y, 20, 20)

        def pos(self):

            if self.direction == 'left':
                self.snake_x -= self.step
            elif self.direction == 'right':
                self.snake_x += self.step
            elif self.direction == 'up':
                self.snake_y -= self.step
            elif self.direction == 'down':
                self.snake_y += self.step
            self.snake_head_rect = pygame.Rect(self.snake_x, self.snake_y, 20, 20)
            self.body_list.append((self.snake_x, self.snake_y))

        def body_del(self):
            del self.body_list[0]

        def snake_move(self):
            self.pos()
            self.snake_head_rect_old = pygame.Rect(self.body_list[0][0], self.body_list[0][1], 20, 20)

            for item in self.body_list:
                screen.fill(ball.random_color, pygame.Rect(item[0], item[1], 20, 20))
            screen.fill((255, 255, 255), self.snake_head_rect_old)
            if not crack():
                self.body_del()
            else:
                ball.add_ball()
            pygame.display.update()

        def eat_ball(self):
            snake.body_list.append((ball.ball_x, ball.ball_y))
            ball.add_ball()
            pygame.display.flip()


    class Ball(object):
        def __init__(self):
            self.ball_rect = pygame.Rect(0, 0, 20, 20)
            self.ball_list = []
            self.ball_x = 100
            self.ball_y = 120
            self.color_list = [(255, 0, 0,), (255, 128, 0), (255, 255, 0), (0, 255, 0), (0, 255, 255), (0, 0, 255),
                               (128, 0, 255)]
            self.random_color = (0, 0, 0)

        def pos(self):
            while True:
                self.ball_x = random.randint(0, 39) * 20
                self.ball_y = random.randint(0, 19) * 20
                if (self.ball_x, self.ball_y) not in snake.body_list:
                    self.ball_list.append((self.ball_x, self.ball_y))
                    return

        def add_ball(self):
            self.pos()
            self.random_color = random.choice(self.color_list)
            self.ball_rect = pygame.Rect(self.ball_x, self.ball_y, 20, 20)
            screen.fill(self.random_color, self.ball_rect)
            pygame.display.update()


    def crack():
        if snake.snake_head_rect[0] == ball.ball_rect[0] and snake.snake_head_rect[1] == ball.ball_rect[1]:
            global score
            score += 1
            return True
        else:
            return False


    def check_dead():
        for i in range(len(snake.body_list) - 1):
            if snake.body_list[i][0] == snake.snake_head_rect[0] and snake.body_list[i][1] == snake.snake_head_rect[
                1]:
                return True
        else:
            if (snake.snake_head_rect[0] < 0 or snake.snake_head_rect[0] > 780) or (
                    snake.snake_head_rect[1] < 0 or snake.snake_head_rect[1] > 460):
                return True


    def get_result():
        if check_dead():
            print(score)



    pygame.init()
    pygame.font.init()
    font = pygame.font.SysFont(None, 50)
    size = width, height = 800, 480
    screen = pygame.display.set_mode(size)
    screen.fill((255, 255, 255))
    snake = Snake()
    ball = Ball()
    ball.add_ball()
    clock = pygame.time.Clock()
    score = 0

    while True:
        for x in range(0, 800, 20):
            pygame.draw.line(screen, (0, 0, 0), (x, 0), (x, 480))
        for y in range(0, 480, 20):
            pygame.draw.line(screen, (0, 0, 0,), (0, y), (800, y))
        time.sleep(0.15)
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and not snake.dead:
                if event.key == pygame.K_LEFT and snake.direction != 'right':
                    snake.direction = 'left'
                elif event.key == pygame.K_DOWN and snake.direction != 'up':
                    snake.direction = 'down'
                elif event.key == pygame.K_UP and snake.direction != 'down':
                    snake.direction = 'up'
                elif event.key == pygame.K_RIGHT and snake.direction != 'left':
                    snake.direction = 'right'

        if check_dead():
            get_result()
            break
        else:
            snake.snake_move()


if __name__ == '__main__':
    process1 = multiprocessing.Process(target=func)
    process2 = multiprocessing.Process(target=func)
    process1.start()
    process2.start()