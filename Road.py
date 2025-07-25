import pygame
from speed_handler import get_road_speed

class Road(pygame.sprite.Sprite):
    
    def __init__(self, groups,road_image,WINDOW_HEIGHT, bottom):
        super().__init__(groups)
        self.image = road_image
        self.rect = self.image.get_frect(bottom=bottom, left = 140)
        self.groups = groups
        self.WINDOW_HEIGHT = WINDOW_HEIGHT
        self.speed = 30
        self.fill_road()


    def update(self, dt):
        self.rect.centery += dt * get_road_speed() * 2
        if(self.rect.top>self.WINDOW_HEIGHT):
            self.kill()
        self.fill_road()

    def fill_road(self):
        road_sprites = self.groups[1].sprites()
        if road_sprites[len(road_sprites) - 1].rect.top > 0:
            Road(self.groups,self.image,self.WINDOW_HEIGHT,self.rect.top)

            