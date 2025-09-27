import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOT_SPEED, PLAYER_SHOOT_COOLDOWN
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0  # in degrees
        self.shoot_counter = 0

    def move(self, dt):
        direction = pygame.Vector2(0, -1).rotate(self.rotation)
        self.position += direction * PLAYER_SPEED * dt


    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt


    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def triangle(self):
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.shoot_counter = max(0, self.shoot_counter - dt)

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        if self.shoot_counter > 0:
            return None
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, -1).rotate(self.rotation) * PLAYER_SHOT_SPEED
        self.shoot_counter = PLAYER_SHOOT_COOLDOWN
        return shot