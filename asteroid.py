import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, SCREEN_WIDTH, SCREEN_HEIGHT

class Asteroid(CircleShape):
    def __init__(self, x,y, radius):
        super().__init__(x, y, radius)
        for group in self.containers:
                group.add(self)
    
    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "white",
            (self.position.x, self.position.y),
            self.radius,
            LINE_WIDTH
        )

    def update(self, dt):
        # Move asteroid according to velocity
        self.position += self.velocity * dt
