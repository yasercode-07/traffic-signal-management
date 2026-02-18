import random

def get_traffic_density(lane):
    """
    Simulates sensor data from 1KM range
    Returns number of vehicles detected
    """
    sensors = 5   # 200m × 5 = 1KM
    
    vehicle_count = 0
    
    for i in range(sensors):
        vehicles = random.randint(5, 40)
        vehicle_count += vehicles
    
    return vehicle_count
