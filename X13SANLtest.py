import smbus
import time

I2C_BUS = 1
DEVICE_ADDR = 0x4D

REG_INPUT     = 0x00
REG_OUTPUT    = 0x01
REG_CONFIG    = 0x03

bus = smbus.SMBus(I2C_BUS)

def set_direction(output_mask):
    """Set GPIO direction. 0 = output, 1 = input"""
    bus.write_byte_data(DEVICE_ADDR, REG_CONFIG, ~output_mask & 0xFF)

def write_outputs(mask):
    """Write to GPIO output register (only affects output pins)"""
    bus.write_byte_data(DEVICE_ADDR, REG_OUTPUT, mask)

def read_inputs():
    """Read GPIO input register"""
    return bus.read_byte_data(DEVICE_ADDR, REG_INPUT)

def read_outputs():
    """Read back last written output value"""
    return bus.read_byte_data(DEVICE_ADDR, REG_OUTPUT)

def test_output():
    # Set GP0-GP3 to output (0), GP4-GP7 to input (1)
    set_direction(0b00001111)  # lower 4 = output, upper 4 = input

    # Set known output pattern
    test_pattern = 0b00000101  # GP0 = High, GP2 = High
    write_outputs(test_pattern)

    time.sleep(0.1)

    # Read back outputs
    out_val = read_outputs()
    print(f"Output register readback: 0b{out_val:08b}")

    # Optional: if looped to inputs, read input register
    in_val = read_inputs()
    print(f"Input register:           0b{in_val:08b}")

    # Assert output values match expected
    assert (out_val & 0x0F) == test_pattern, "Output mismatch!"

    print("Test passed.")

if __name__ == "__main__":
    test_output()
