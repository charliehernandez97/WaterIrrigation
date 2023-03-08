from pymodbus.client.sync import ModbusTcpClient
import time
import random


client = ModbusTcpClient('172.20.10.8')
client.connect()

def manage_tank_level(tank_value : int, max_tank_value : int):
    meter = "#" * max_tank_value
    print("Current Tank Level", end=" ")
    print("\tMeter")
    print(tank_value, end=" ")
    print("\t\t\t" + meter[0:tank_value])

    coils = client.read_coils(0,6)
    is_tank_full = coils.bits[3]
    is_tank_empty = coils.bits[5]

    if is_tank_empty:
        coils = client.write_coil(2, 1)
    elif is_tank_full:
        coils = client.write_coil(2, 0)


while True:
    holding_registers = client.read_holding_registers(0, 3)
    max_tank_level = holding_registers.registers[0]
    current_tank_level = holding_registers.registers[2]
    manage_tank_level(current_tank_level, max_tank_level)
    time.sleep(1)