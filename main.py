import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

VERSION = pygame.version.ver

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
fps, dt = pygame.time.Clock(), 0

#groups
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()

#Player setup
Player.containers = (updatable, drawable)
player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

#Asteroid & Field setup
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable,)
asteroidfield = AsteroidField()

running = True

while running:
    log_state()
    dt = fps.tick(60) / 1000

    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Update Updatable
    updatable.update(dt)

    #Draw all drawable
    screen.fill("black")
    for obj in drawable:
        obj.draw(screen)
    
    pygame.display.flip()

def main():
    print(f"Starting Asteroids with pygame version: {VERSION}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
    
