from pymodbus.client.sync import ModbusTcpClient
import time
import random

client = ModbusTcpClient('192.168.1.67')
client.connect()

TURN_ON = 1
TURN_OFF = 0
OUTGOING_VALVE = 0
INCOMING_VALVE = 2
MOISTURE_ADDRESS = 3
MANUAL = 6

plant_moisture = 10
max_moisture = 10
meter = "##########"
dry = False
while True:
    print("Plant Moisture", end=" ")
    print("\tMeter")
    print(plant_moisture, end=" ")
    print("\t\t\t\t\t\t\t" + meter[0:plant_moisture])

    coils = client.read_coils(0,6)
    registers = client.read_holding_registers(0,6)

    is_pump_on = coils.bits[1]
    is_tank_full = coils.bits[3]
    is_tank_empty = coils.bits[5]
    manual = coils.bits[6]
    moisture_register = registers.getRegister(3)

    # used to simulate plant moisture going down
    # at random times between 2 and 10
    random_time = random.randint(2, 8)

    if manual:
        if not is_pump_on:
            plant_moisture -= 1
            registers = client.write_register(MOISTURE_ADDRESS, plant_moisture)
            time.sleep(2)
        else:
            plant_moisture += 1 
            registers = client.write_register(MOISTURE_ADDRESS, plant_moisture)
            time.sleep(0.5)
    else:
        if not is_pump_on:
            plant_moisture -= 1
            registers = client.write_register(MOISTURE_ADDRESS, plant_moisture)

            if plant_moisture == 0:
                dry = True
            
            time.sleep(random_time)
        if dry:
            plant_moisture += 1
            registers = client.write_register(MOISTURE_ADDRESS, plant_moisture)
            coils = client.write_coil(OUTGOING_VALVE, TURN_ON)

        if plant_moisture == 10:
            dry = False
            coils = client.write_coil(OUTGOING_VALVE, TURN_OFF)
        elif is_tank_empty:
            coils = client.write_coil(OUTGOING_VALVE, TURN_OFF)
        
        time.sleep(0.5)

    if plant_moisture > max_moisture:
        plant_moisture = max_moisture
    elif plant_moisture < 0:
        plant_moisture = 0

    