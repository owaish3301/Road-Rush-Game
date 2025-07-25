speed_multiplier = 100
max_player_speed = 200

def speed_increment():
    global speed_multiplier
    if speed_multiplier <= 100:
        speed_multiplier += 2.0

def get_speed_multiplier():
    global speed_multiplier
    return speed_multiplier

def decrease_speed_multiplier():
    global speed_multiplier
    if speed_multiplier >= 25:
        speed_multiplier -= 1.0

def get_player_speed():
    min_speed = 50
    speed_range = max_player_speed - min_speed  
    multiplier_range = 100 - 25 
    
    return min_speed + (speed_range * (speed_multiplier - 25) / multiplier_range)

def get_road_speed():
    min_road_speed = 37.5 
    max_road_speed = 150
    speed_range = max_road_speed - min_road_speed
    multiplier_range = 100 - 25
    
    return min_road_speed + (speed_range * (speed_multiplier - 25) / multiplier_range)