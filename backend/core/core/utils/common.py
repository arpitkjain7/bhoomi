sensor_height = 19
levels = 10


def getWaterLevel(water_distance: str):
    height_of_level = sensor_height / levels
    water_level_in_cm = sensor_height - water_distance
    water_level = round(water_level_in_cm / height_of_level, 2)
    return water_level
