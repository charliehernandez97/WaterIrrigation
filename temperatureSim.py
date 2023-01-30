import random
import time

# TODO turn this into a function that returns temp value

# temp = 72.0

# Temperature range
min_temp = 32.0
max_temp = 100.0

# Temperature change range
min_change = -4
max_change = 4


def modified_temp(current_temp):
    # Generate a random temperature change
    temp_change = random.randint(min_change, max_change)
    current_temp += temp_change

    # Check if temperature is within range
    if current_temp > max_temp:
        current_temp = max_temp
    elif current_temp < min_temp:
        current_temp = min_temp

    return current_temp


time.sleep(1)
