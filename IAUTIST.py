import pygame
import sys

# Настройки экрана
WIDTH, HEIGHT = 800, 600
WHITE = (255, 0, 255)
BLACK = (0, 255, 255)
BLUE = (0, 250, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Пинг-понг")
clock = pygame.time.Clock()

# Класс для ракеток (Спрайты)
class Paddle():
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 15, 90)
        self.speed = 7

    def move(self, up_key, down_key):
        keys = pygame.key.get_pressed()
        if keys[up_key] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[down_key] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed

    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect)

# Класс для мяча
class Ball():
    def __init__(self):
        self.rect = pygame.Rect(WIDTH//2, HEIGHT//2, 15, 15)
        self.speed_x = 5
        self.speed_y = 5

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Отскок от верхней и нижней стенок (Действия)
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed_y *= -1

    def draw(self):
        pygame.draw.ellipse(screen, BLUE, self.rect)

# Создание объектов
player_left = Paddle(20, HEIGHT//2 - 45)
player_right = Paddle(WIDTH - 35, HEIGHT//2 - 45)
ball = Ball()

# Основной цикл игры
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Движение (Управление по схеме)
    player_left.move(pygame.K_w, pygame.K_s) # Левая: W и S
    player_right.move(pygame.K_UP, pygame.K_DOWN) # Правая: Стрелки
    ball.move()

    # Столкновение ракетки и мяча (Действия)
    if ball.rect.colliderect(player_left.rect) or ball.rect.colliderect(player_right.rect):
        ball.speed_x *= -1

    # Проигрыш при касании боковой стены (Действия)
    if ball.rect.left <= 0 or ball.rect.right >= WIDTH:
        break

    # Отрисовка
    screen.fill(BLACK)
    player_left.draw()
    player_right.draw()
    ball.draw()
    
    pygame.display.flip()
    clock.tick(60)