import serial

ser = serial.Serial(
    port="/dev/ttyUSB0",
    baudrate=2400,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

ser.write(0x09)

while True:
    print(ser.read(size=6))