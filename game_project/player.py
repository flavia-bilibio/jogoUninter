import pygame


class Player:
    def __init__(self):
        self.x = 300
        self.y = 380
        self.speed = 5

        self.image = pygame.image.load("assets/images/player.png")
        self.image = pygame.transform.scale(self.image, (40, 40))

        self.width = 40
        self.height = 40

    def move_left(self):
        self.x -= self.speed

    def move_right(self):
        self.x += self.speed

    def move_up(self):
        self.y -= self.speed

    def move_down(self):
        self.y += self.speed

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.move_left()
        if keys[pygame.K_RIGHT]:
            self.move_right()
        if keys[pygame.K_UP]:
            self.move_up()
        if keys[pygame.K_DOWN]:
            self.move_down()

        self.x = max(0, min(self.x, 600 - self.width))
        self.y = max(0, min(self.y, 480 - self.height))

    def draw(self):
        screen = pygame.display.get_surface()
        screen.blit(self.image, (self.x, self.y))