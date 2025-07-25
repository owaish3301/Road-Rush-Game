distance = 0

def get_player_distance():
    global distance
    return distance


def calculate_player_distance(time, speed):
    global distance
    distance += speed * time