import pygame
import circleshape
import random

from constants import ASTEROID_MIN_RADIUS

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
        # self.velocity = pygame.Vector2(1, 0).rotate(angle) * ASTEROID_SPEED

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return []
        else:
            rand_angle = random.uniform(20,50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = self.velocity.rotate(rand_angle) * 1.2
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2.velocity = self.velocity.rotate(-rand_angle) * 1.2
            return [asteroid1, asteroid2]

    