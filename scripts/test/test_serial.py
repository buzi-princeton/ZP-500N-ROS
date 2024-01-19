import serial
import time

ser = serial.Serial(
    port="/dev/ttyUSB0",
    baudrate=2400,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

cur_time = time.time()
for i in range(100):
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
print("Elapsed time: {}".format((time.time() - cur_time)*0.01))