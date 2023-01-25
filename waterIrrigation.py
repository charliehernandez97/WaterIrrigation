import time
import keyboard

# TODO
"""
this file will be modified to simulate moisture of plants
using the humidity and temp sim
"""

soil_moisture = 10
meter = "##########"

print("This is a simple irrigation simulation")

while True:
    print("Soil Moisture", end=" ")
    print("\tMeter")
    print(soil_moisture, end=" ")
    print("\t\t\t\t" + meter[0:soil_moisture])

    if not keyboard.is_pressed('w'):
        if soil_moisture != 0:
            soil_moisture -= 1
        else:
            print("WARNING! SOIL MOISTURE LOW")

    if keyboard.is_pressed('w') and soil_moisture != 10:
        soil_moisture += 1

    time.sleep(1.5)


