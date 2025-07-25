import pygame
from speed_handler import speed_increment

class Player(pygame.sprite.Sprite):
    def __init__(self, groups, player_image):
        super().__init__(groups)
        self.image = player_image
        self.rect = self.image.get_frect(center = (150,650))
        self.direction = pygame.math.Vector2()
        self.lateral_speed = 100


    def update(self,dt):
        if self.rect.left <= 140:
            self.rect.left = 140
        if self.rect.right >= 350:
            self.rect.right = 350

        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
        # self.direction.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])
        if(keys[pygame.K_w]):
            speed_increment()
        self.direction = self.direction.normalize() if self.direction else self.direction
        self.rect.center += self.direction * self.lateral_speed * dt * 2.5
        
