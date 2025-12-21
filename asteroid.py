import pygame, random
from circleshape import CircleShape
from logger import log_event
from constants import LINE_WIDTH, SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x,y, radius):
        super().__init__(x, y, radius)
        for group in self.containers:
                group.add(self)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        r_angle = random.uniform(20, 50)
        vel1 = self.velocity.rotate(r_angle) * 1.2
        vel2 = self.velocity.rotate(-r_angle) * 1.2
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position, self.velocity, new_radius)
        asteroid1.velocity = vel1
        asteroid2 = Asteroid(self.position, self.velocity, new_radius)
        asteroid2.velocity = vel2

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "white",
            (self.position[0], self.position[1]),
            self.radius,
            LINE_WIDTH
        )

    def update(self, dt):
        # Move asteroid according to velocity
        self.position += self.velocity * dt
