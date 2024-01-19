Python wrapper and ROS wrapper for the ZP-500N dynamometer that I bought for my research, using pyserial.

For now, it seems like the sampling rate (from serial) is 10 Hz.

To run the publisher node: Run the test_serial.py to make sure that the measurement unit is plugged in and properly read. Run the following node:

```
rosrun zp_500n_ros dynamometer_publisher.py
```