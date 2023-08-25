import serial
import time

ser = serial.Serial(
    port="/dev/ttyUSB0",
    baudrate=2400,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

while True:
    try:
        data = float(ser.read(size=6).decode('utf-8'))
        print(data)
    except KeyboardInterrupt:
        break
    except:
        print("Fix error buffer")
        while True:
            try:
                data = float(ser.read(size=6).decode('utf-8'))
                break
            except:
                print("Flush 1 byte, {}".format(ser.read(size=1)))
                continue
