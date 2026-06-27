import pygame
from player import Player
from obstacle import Obstacle
from rainbow import Rainbow
from collisionManager import CollisionManager


class Game:
    def __init__(self):
        self.running = True
        self.score = 0
        self.goal = 10

        self.state = "menu"

        self.player = Player()
        self.obstacles = [Obstacle() for _ in range(3)]
        self.rewards = [Rainbow() for _ in range(3)]

        self.collision_manager = CollisionManager()

        self.screen = None
        self.clock = pygame.time.Clock()

        self.background = None

    def start(self):
        pygame.init()
        pygame.mixer.init()

        self.screen = pygame.display.set_mode((600, 480))
        pygame.display.set_caption("Star Chaser")

        self.background = pygame.image.load("assets/images/background.png")
        self.background = pygame.transform.scale(self.background, (600, 480))

        pygame.mixer.music.load("assets/audio/music.wav")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

        self.game_loop()

    def game_loop(self):
        while self.running:
            self.clock.tick(60)

            self.handle_events()

            if self.state == "menu":
                self.menu()

            elif self.state == "playing":
                self.update()
                self.check_collisions()
                self.render()

            elif self.state == "win":
                self.win_screen()

            elif self.state == "gameover":
                self.gameover_screen()

        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN and self.state == "menu":
                    self.state = "playing"

                if event.key == pygame.K_r:
                    if self.state in ["gameover", "win"]:
                        self.restart()

    def update(self):
        self.player.update()

        for obstacle in self.obstacles:
            obstacle.update()

        for reward in self.rewards:
            reward.update()

    def check_collisions(self):
        for reward in self.rewards:
            if self.collision_manager.check_player_reward(self.player, reward):
                self.score += 1
                reward.respawn()

        if self.score >= self.goal:
            self.win()

        for obstacle in self.obstacles:
            if self.collision_manager.check_player_obstacle(self.player, obstacle):
                self.game_over()

    def render(self):
        self.screen.blit(self.background, (0, 0))

        self.player.draw()

        for obstacle in self.obstacles:
            obstacle.draw()

        for reward in self.rewards:
            reward.draw()

        font = pygame.font.SysFont(None, 30)
        score_text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))

        pygame.display.update()

    def menu(self):
        self.screen.blit(self.background, (0, 0))

        title_font = pygame.font.SysFont(None, 48)
        text_font = pygame.font.SysFont(None, 30)

        title = title_font.render("STAR CHASER", True, (0, 0, 0))
        start = text_font.render("Press ENTER to start", True, (0, 0, 0))
        controls1 = text_font.render("Arrow Keys - Move", True, (0, 0, 0))
        controls2 = text_font.render("Collect 10 stars and avoid obstacles!", True, (0, 0, 0))

        self.screen.blit(title, (170, 120))
        self.screen.blit(start, (175, 200))
        self.screen.blit(controls1, (190, 260))
        self.screen.blit(controls2, (110, 300))

        pygame.display.update()

    def game_over(self):
        self.state = "gameover"

    def win(self):
        self.state = "win"

    def restart(self):
        self.score = 0

        self.player = Player()
        self.obstacles = [Obstacle() for _ in range(3)]
        self.rewards = [Rainbow() for _ in range(3)]

        self.state = "menu"

    def win_screen(self):
        self.screen.fill((0, 0, 0))

        title_font = pygame.font.SysFont(None, 60)
        text_font = pygame.font.SysFont(None, 30)

        title = title_font.render("YOU WIN!", True, (0, 255, 0))
        score = text_font.render(f"Score: {self.score}", True, (255, 255, 255))
        restart = text_font.render("Press R to restart", True, (255, 255, 255))

        y = 150 + (pygame.time.get_ticks() // 10 % 10)

        self.screen.blit(title, (180, y))
        self.screen.blit(score, (220, 240))
        self.screen.blit(restart, (170, 300))

        pygame.display.update()

    def gameover_screen(self):
        self.screen.fill((0, 0, 0))

        title_font = pygame.font.SysFont(None, 60)
        text_font = pygame.font.SysFont(None, 30)

        title = title_font.render("GAME OVER", True, (255, 0, 0))
        score = text_font.render(f"Score: {self.score}", True, (255, 255, 255))
        restart = text_font.render("Press R to restart", True, (255, 255, 255))

        self.screen.blit(title, (150, 150))
        self.screen.blit(score, (220, 240))
        self.screen.blit(restart, (170, 300))

        pygame.display.update()