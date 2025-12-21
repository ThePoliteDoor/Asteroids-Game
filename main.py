import pygame, sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

VERSION = pygame.version.ver

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
fps, dt = pygame.time.Clock(), 0

#groups
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

#Player setup
Player.containers = (updatable, drawable)
player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

#Asteroid & Field setup
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable,)
asteroidfield = AsteroidField()

#shots
Shot.containers = (shots, updatable, drawable)

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

    for asteroid  in asteroids:
        if asteroid.collides_with(player):
            log_event("player_hit")
            print("Game Over!")
            sys.exit()

    for asteroid  in asteroids:
        for shot in shots:
            if asteroid.collides_with(shot):
                log_event("asteroid_shot")
                asteroid.split()
                shot.kill()


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
    
