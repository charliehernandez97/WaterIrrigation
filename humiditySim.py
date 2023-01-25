import random
import time

# TODO turn this into a function that returns humidity value

# Initial humidity
humidity = 60

# Humidity range
min_humidity = 20
max_humidity = 90

# Humidity change range
min_change = -3
max_change = 3

while True:
    # Generate a random humidity change
    humidity_change = random.randint(min_change, max_change)
    humidity += humidity_change

    # Check if humidity is within range
    if humidity > max_humidity:
        humidity = max_humidity
    elif humidity < min_humidity:
        humidity = min_humidity

    print("Humidity:", humidity)
    time.sleep(1)
