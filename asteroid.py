import pygame
import random
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.name = "asteroid"
        Asteroid.containers.add(self)


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def destory(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        for _ in range(2):
            radius = self.radius - random.randint(10, ASTEROID_MIN_RADIUS) 
            move = random.randint(-15, 15)
            rotate = random.randint(20, 50)
            asteroid = Asteroid(self.position.x + move, self.position.y + move, radius)
            asteroid.velocity = self.velocity.rotate(rotate) * 1.2
