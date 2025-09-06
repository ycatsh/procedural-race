import pygame

from constants import *
from car import Car
from track import Track


pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))


class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.running = True
        self.track = Track(screen_width=WIDTH, screen_height=HEIGHT)
        self.car = Car(x=WIDTH//2, y=HEIGHT-100)
        self.font = pygame.font.SysFont(None, 60)
        self.state = "play"

    def run(self):
        while self.running:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN and self.state == "gameover":
                    self.running = False

            if self.state == "play":
                keys = pygame.key.get_pressed()
                track_edges = self.track.get_edges_at_car(self.car.y + self.car.height) 
                self.car.update(keys, track_edges)

                if self.car.collided:
                    self.state = "gameover"

                self.track.update(WIDTH, HEIGHT)

                SCREEN.fill(GRAY)
                self.track.draw(SCREEN, WIDTH)
                self.car.draw(SCREEN)

            elif self.state == "gameover":
                SCREEN.fill(BLACK)
                text = self.font.render("GAME OVER", True, GRAY)
                desc = self.font.render("Press any key to quit", True, GRAY)

                SCREEN.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - 50))
                SCREEN.blit(desc, (50, HEIGHT // 2))

            pygame.display.flip()

        pygame.quit()

if __name__ == "__main__":
    Game().run()
