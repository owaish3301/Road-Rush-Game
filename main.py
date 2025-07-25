import pygame
from os.path import join

from Road import Road
from Player import Player
from Car import Car, get_smart_car_location, check_spawn_safety
from speed_handler import decrease_speed_multiplier, get_player_speed
from player_distance_calculator import get_player_distance, calculate_player_distance

pygame.init()

clock = pygame.time.Clock()

running = True

WINDOW_HEIGHT = 720
WINDOW_WIDTH = 480
display_surf = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Road Rush")

all_sprites = pygame.sprite.Group()
road_sprites = pygame.sprite.Group()
player_sprite = pygame.sprite.Group()
car_sprites = pygame.sprite.Group()

road_image = pygame.image.load(join('images','road.jpg')).convert()
Road((all_sprites, road_sprites),road_image, WINDOW_HEIGHT,WINDOW_HEIGHT)

bike_image = pygame.transform.scale(pygame.image.load(join('images','bike.png')).convert_alpha(),(30,50))
player = Player((all_sprites,player_sprite), bike_image)

car_image = pygame.transform.scale(pygame.image.load(join('images','car.png')).convert_alpha(),(90,100))



font = pygame.font.Font(None,30)

last_car_spawn_time = pygame.time.get_ticks()

def can_spawn_car():
    global last_car_spawn_time
    if pygame.time.get_ticks() - last_car_spawn_time  > 100000/get_player_speed():
        last_car_spawn_time = pygame.time.get_ticks()
        return True
    else:
        return False

while running:
    dt = clock.tick() / 1000
    decrease_speed_multiplier()
    calculate_player_distance(dt, get_player_speed())
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running = False
    
    all_sprites.update(dt)

    display_surf.fill('#36c651')


    road_sprites.draw(display_surf)
    player_sprite.draw(display_surf)
    if can_spawn_car() == True:
        smart_position = get_smart_car_location(car_sprites.sprites())
        if smart_position is not None:
            if check_spawn_safety(car_sprites.sprites(), smart_position):
                Car((all_sprites, car_sprites), car_image, WINDOW_HEIGHT, smart_position)
    car_sprites.draw(display_surf)

    
    if pygame.sprite.spritecollide(player, car_sprites, False, pygame.sprite.collide_mask):
        running = False

    score_surf1 = font.render("Top speed : 200", True, "black")
    score_surf2 = font.render(f"Current Speed : {get_player_speed():.1f}", True, "black")
    score_surf3 = font.render(f"Distance Covered : {get_player_distance():.1f}", True, "black")
    score_rect1 = score_surf1.get_frect(top=20, right=WINDOW_WIDTH-20)
    score_rect2 = score_surf2.get_frect(top=40, right=WINDOW_WIDTH-20)
    score_rect3 = score_surf3.get_frect(top=60, right=WINDOW_WIDTH-20)
    
    display_surf.blit(score_surf1, score_rect1)
    display_surf.blit(score_surf2, score_rect2)
    display_surf.blit(score_surf3, score_rect3)
    pygame.display.update()

pygame.quit()
