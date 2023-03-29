from pymodbus.client import ModbusTcpClient
import time
import random

TURN_ON = 1
TURN_OFF = 0
OUTGOING_VALVE = 0
INCOMING_VALVE = 2
MANUAL = 6

client = ModbusTcpClient('192.168.1.215')
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
        coils = client.write_coil(INCOMING_VALVE, TURN_ON)
        coils = client.write_coil(OUTGOING_VALVE, TURN_OFF)
    elif is_tank_full:
        coils = client.write_coil(INCOMING_VALVE, TURN_OFF)


while True:
    holding_registers = client.read_holding_registers(0, 3)
    max_tank_level = holding_registers.registers[0]
    current_tank_level = holding_registers.registers[2]
    manage_tank_level(current_tank_level, max_tank_level)
    time.sleep(1)