import smbus
import time

LightMeter = 0x23
HihgResMode = 0x20
bus = smbus.SMBus(1)

def Int_converter(data):
    return ((data[1] + (256 * data[0])) / 1.2)
 

def LightInput(addr=LightMeter):
    result = bus.read_i2c_block_data(addr,HihgResMode)
    return Int_converter(result)

max = 400
medium = 50
low = 25
min = 15

def LightCheck():
    temp_light = LightInput()
    if temp_light > max:
        print("TOO BRIGHT")
    elif temp_light <= max and temp_light > medium:
        print("BRIGHT")
    elif temp_light <= medium and temp_light > low:
        print("MEDIUM")
    elif temp_light <= low and temp_light > min:
        print("DARK")
    else:
        print("too dark")
    time.sleep(3)


def main():
    while True:
        LightCheck()

if __name__=="__main__":
   main()
