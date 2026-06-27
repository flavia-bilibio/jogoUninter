import pygame
import random


class Rainbow:
    def __init__(self):
        self.x = random.randint(50, 550)
        self.y = random.randint(50, 400)

        self.collected = False

        self.image = pygame.image.load("assets/images/rainbow.png")
        self.image = pygame.transform.scale(self.image, (30, 30))

        self.width = 30
        self.height = 30

    def update(self):
        pass

    def draw(self):
        screen = pygame.display.get_surface()
        screen.blit(self.image, (self.x, self.y))

    def respawn(self):
        self.x = random.randint(50, 550)
        self.y = random.randint(50, 400)
        self.collected = False

    def on_collect(self):
        self.collected = True
        self.respawn()