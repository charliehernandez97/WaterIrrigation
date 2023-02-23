from pymodbus.client.sync import ModbusTcpClient
import time
import random

client = ModbusTcpClient('192.168.1.215')
client.connect()

plant_moisture = 5
max_moisture = 10
meter = "##########"
dry = False
while True:
    print("Plant Moisture", end=" ")
    print("\tMeter")
    print(plant_moisture, end=" ")
    print("\t\t" + meter[0:plant_moisture])

    coils = client.read_coils(0,6)
    is_pump_on = coils.bits[1]
    is_tank_full = coils.bits[3]
    is_tank_empty = coils.bits[5]

    # used to simulate plant moisture going down
    # at random times between 2 and 10
    random_time = random.randint(2, 10)

    if not is_pump_on:
        plant_moisture -= 1

        if plant_moisture == 0:
            dry = True
    
    if dry and not is_tank_empty:
        plant_moisture += 1
        coils = client.write_coil(0,1)

        if plant_moisture > 8:
            dry = False
            coils = client.write_coil(0,0)

    if plant_moisture > max_moisture:
        plant_moisture = max_moisture
    elif plant_moisture < 0:
        plant_moisture = 0

    time.sleep(1)