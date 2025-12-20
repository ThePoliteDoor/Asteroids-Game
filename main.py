import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

VERSION = pygame.version.ver

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
fps = pygame.time.Clock()
dt = 0
x = SCREEN_WIDTH / 2
y = SCREEN_HEIGHT / 2
player = Player(x, y)


running = True

while running:
    log_state()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")
    player.update(dt)
    player.draw(screen)
    
    pygame.display.flip()

    dt = fps.tick(60) / 1000

def main():
    print(f"Starting Asteroids with pygame version: {VERSION}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
    
