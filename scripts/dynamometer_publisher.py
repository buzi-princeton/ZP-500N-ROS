import rospy
from zp_500n_ros.msg import Float32
import serial

ser = serial.Serial(
    port="/dev/ttyUSB0",
    baudrate=2400,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

def dynamometer_publisher():
    pub = rospy.Publisher('zp_500n', Float32, queue_size=10)
    rospy.init_node('zp_500n_pub', anonymous=True)
    rate = rospy.Rate(20)
    while not rospy.is_shutdown():
        try:
            data = float(ser.read(size=6).decode('utf-8'))
            # print(data)
        except:
            print("Fix error buffer")
            while True:
                try:
                    data = float(ser.read(size=6).decode('utf-8'))
                    break
                except:
                    print("Flush 1 byte, {}".format(ser.read(size=1)))
                    continue
        rospy.loginfo(data)
        msg = Float32()
        msg.data = data
        pub.publish(msg)
        rate.sleep()
    
if __name__ == "__main__":
    try:
        dynamometer_publisher()
    except rospy.ROSInterruptException:
        pass