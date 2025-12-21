import pygame
from math import sqrt

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def collides_with(self, other):
        distance = sqrt(
            ((self.position[0] - other.position[0]) ** 2) +
            ((self.position[1] - other.position[1]) ** 2)
        )
        return distance <= (self.radius + other.radius)

    def draw(self, screen):
        # must override
        pass

    def update(self, dt):
        # must override
        pass
