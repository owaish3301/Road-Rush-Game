import pygame
import random
from speed_handler import get_road_speed

class Car(pygame.sprite.Sprite):
    def __init__(self, groups, image, WINDOW_HEIGHT, position=None):
        super().__init__(groups)
        self.image = image
        if position is not None:
            self.rect = self.image.get_frect(top=-50, left=position)
        else:
            self.rect = self.image.get_frect(top=-50, left=get_car_location())
        self.WINDOW_HEIGHT= WINDOW_HEIGHT

    def update(self, dt):
        if self.rect.top>self.WINDOW_HEIGHT:
            self.kill()
        self.rect.centery += dt * get_road_speed() * 1.2 * 2


CAR_SPAWN_POSITIONS = [150, 180, 210, 240, 250]


MIN_CAR_DISTANCE = 100

MIN_GAP_WIDTH = 90

def get_car_location():
    return random.choice(CAR_SPAWN_POSITIONS)

def get_smart_car_location(existing_cars):
    if not existing_cars:
        return random.choice(CAR_SPAWN_POSITIONS)
    
    nearby_cars = []
    for car in existing_cars:
        if car.rect.top <= 200:
            nearby_cars.append(car.rect.centerx)
    
    if not nearby_cars:
        return random.choice(CAR_SPAWN_POSITIONS)

    available_positions = []
    
    for pos in CAR_SPAWN_POSITIONS:
        is_safe = True
        
        for car_x in nearby_cars:
            if abs(pos - car_x) < MIN_CAR_DISTANCE:
                is_safe = False
                break
        
        if is_safe:
            available_positions.append(pos)

    if available_positions:
        if len(available_positions) == 0:
            return None
            
        available_positions.sort()
        
        if len(available_positions) < 2 and len(nearby_cars) >= 3:
            return None
            
        return random.choice(available_positions)
    
    return None

def check_spawn_safety(existing_cars, potential_position):
    if not existing_cars:
        return True

    cars_in_spawn_area = 0
    occupied_positions = []
    
    for car in existing_cars:
        if car.rect.top <= 150:
            cars_in_spawn_area += 1
            occupied_positions.append(car.rect.centerx)
    
    if cars_in_spawn_area >= 3:
        return False
    
    occupied_positions.append(potential_position)
    occupied_positions.sort()
    
    gaps = []
    for i in range(len(occupied_positions) - 1):
        gap = occupied_positions[i + 1] - occupied_positions[i]
        gaps.append(gap)
    
    min_required_gap = MIN_GAP_WIDTH
    has_safe_gap = any(gap >= min_required_gap for gap in gaps)
    
    left_edge_gap = occupied_positions[0] - 140 
    right_edge_gap = 350 - occupied_positions[-1]  
    
    if left_edge_gap >= min_required_gap or right_edge_gap >= min_required_gap:
        has_safe_gap = True
    
    return has_safe_gap
