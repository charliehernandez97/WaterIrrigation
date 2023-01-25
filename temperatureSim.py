import random
import time

# TODO turn this into a function that returns temp value

# Initial temperature
temp = 72.0

# Temperature range
min_temp = 32.0
max_temp = 100.0

# Temperature change range
min_change = -4
max_change = 4

while True:
    # Generate a random temperature change
    temp_change = random.randint(min_change, max_change)
    temp += temp_change

    # Check if temperature is within range
    if temp > max_temp:
        temp = max_temp
    elif temp < min_temp:
        temp = min_temp

    print("Temperature:", temp)
    time.sleep(1)
