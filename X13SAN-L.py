import smbus
import time

I2C_BUS = 1                   # Usually 1 on Raspberry Pi or similar SBC
DEVICE_ADDR = 0x4D            # PCA9554 I2C address
REG_OUTPUT = 0x01             # Output port register
REG_CONFIG = 0x03             # Configuration register

bus = smbus.SMBus(I2C_BUS)

# Set all pins to output (0 = output, 1 = input)
direction_mask = 0b11110000
bus.write_byte_data(DEVICE_ADDR, REG_CONFIG, direction_mask)

# Set output value for GP0-GP3 
output_mask = 0b00000101
bus.write_byte_data(DEVICE_ADDR, REG_OUTPUT, output_mask)

print("GPIOs configured and output written.")

#set GP0–GP3 as outputs, GP4–GP7 as inputs

# write a value of 0b00000101 to the output register: this sets GP0 = High, GP1 = Low, GP2 = High, GP3 = Low

# Input pins can be read using the input register (0x00) if needed

