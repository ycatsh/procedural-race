import pygame

from constants import *

class Car:
    def __init__(self, x, y):
        self.width, self.height = 20, 40
        self.x, self.y = x, y
        self.vel_x = 0
        self.angle = 0
        self.acceleration = 0.3
        self.friction = 0.15
        self.max_speed = 4
        self.turn_speed = 1
        self.collided = False

    def update(self, keys, track_edges):
        if keys[pygame.K_a]:
            self.vel_x -= self.acceleration
            self.angle = max(25, self.angle - self.turn_speed)

        elif keys[pygame.K_d]:
            self.vel_x += self.acceleration
            self.angle = min(-25, self.angle + self.turn_speed)
            
        else:
            if abs(self.vel_x) >= self.friction:
                self.vel_x -= self.friction * (1 if self.vel_x > 0 else -1)
            else:
                self.vel_x = 0
            if abs(self.angle) >= self.turn_speed:
                self.angle -= self.turn_speed * (1 if self.angle > 0 else -1)
            else:
                self.angle = 0

        self.vel_x = max(-self.max_speed, min(self.max_speed, self.vel_x))
        self.x += self.vel_x

        left_edge, right_edge = track_edges
        if self.x < left_edge or self.x + self.width > right_edge:
            self.collided = True 

    def draw(self, screen):
        car_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        car_surface.fill(RED)
        rotated = pygame.transform.rotate(car_surface, self.angle)
        rect = rotated.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        screen.blit(rotated, rect.topleft)