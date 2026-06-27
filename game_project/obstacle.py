import pygame
import random


class Obstacle:
    def __init__(self):
        self.x = random.randint(50, 550)
        self.y = random.randint(-300, -50)

        self.speed = 4

        self.image = pygame.image.load("assets/images/obstacle.png")
        self.image = pygame.transform.scale(self.image, (40, 40))

        self.width = 40
        self.height = 40

    def update(self):
        self.y += self.speed

        if self.y > 480:
            self.reset_position()

    def draw(self):
        screen = pygame.display.get_surface()
        screen.blit(self.image, (self.x, self.y))

    def reset_position(self):
        self.x = random.randint(50, 550)
        self.y = random.randint(-300, -50)