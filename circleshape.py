import pygame


class CircleShape(pygame.sprite.Sprite):
    containers = pygame.sprite.Group()
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
        self.name = ""

    def draw(self, screen):
        # must override
        pass

    def update(self, dt):
        # must override
        pass

    def isCollided(self, circle):
        if self.position.distance_to(circle.position) < self.radius + circle.radius:
            if self.name == "shot" and circle.name == "asteroid":
                return True
            if self.name == "player" and circle.name == "asteroid":
                return True
