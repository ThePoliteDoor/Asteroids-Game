import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x,y):
        super().__init__(x, y, SHOT_RADIUS)
        for group in self.containers:
                group.add(self)
    
    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "white",
            self.position,
            self.radius,
            LINE_WIDTH
        )

    def update(self, dt):
        # Move asteroid according to velocity
        self.position += self.velocity * dt