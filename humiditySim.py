import random
import time

# TODO turn this into a function that returns humidity value

# humidity = 60

# Humidity range
min_humidity = 20
max_humidity = 90

# Humidity change range
min_change = -3
max_change = 3


def modified_humidity(current_humidity):
    # Generate a random humidity change
    humidity_change = random.randint(min_change, max_change)
    current_humidity += humidity_change

    # Check if humidity is within range
    if current_humidity > max_humidity:
        current_humidity = max_humidity
    elif current_humidity < min_humidity:
        current_humidity = min_humidity

    return current_humidity


time.sleep(1)
