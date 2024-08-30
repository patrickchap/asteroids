import pygame
from constants import *
from circleshape import CircleShape


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.position = pygame.Vector2(x, y)
        self.radius = PLAYER_RADIUS
        self.rotation = 0
        Player.containers.add(self)

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def rotate(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rotation -= PLAYER_TURN_SPEED * dt
        if keys[pygame.K_RIGHT]:
            self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        self.rotate(dt)
        self.move(dt)

    def move(self, dt):
        keys = pygame.key.get_pressed()
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        if keys[pygame.K_UP]:
            if self.position.x < 0:
                self.position.x = SCREEN_WIDTH
            if self.position.x > SCREEN_WIDTH:
                self.position.x = 0 
            if self.position.y < 0:
                self.position.y = SCREEN_HEIGHT
            if self.position.y > SCREEN_HEIGHT:
                self.position.y = 0
            self.position += forward * PLAYER_SPEED * dt
        if keys[pygame.K_DOWN]:
            self.position -= forward * PLAYER_SPEED * dt
