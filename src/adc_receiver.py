#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import UInt16
import serial

rospy.init_node('sensor_publisher', anonymous=True)

if rospy.has_param('serial_device'):
     rospy.loginfo("'serial_device' got from parameter sever")
     dev_name = rospy.get_param('serial_device', '/dev/ttyACM0')
else:
     rospy.loginfo("'serial_device' not found, Use default")
     dev_name = '/dev/ttyACM1'
    
ser = serial.Serial(dev_name, 115200, timeout=1) # Establish the connection on a specific port
rospy.loginfo("Wait 2s for establish the connection")
rospy.sleep(2)
counter = 0 # Reading counter


pub = rospy.Publisher('sensor_chatter', String, queue_size = 1000)
# Publisher for individual channels
adc0_pub = rospy.Publisher("adc0_chatter", UInt16, queue_size = 100)
adc1_pub = rospy.Publisher("adc1_chatter", UInt16, queue_size = 100)

rospy.loginfo("start reading")
ser.write('a')

while True:
     counter +=1
     #ser.write('a') # Convert the decimal number to ASCII then send it to the Arduino
     readings = ser.readline() # Read the newest output from the Arduino
     #rospy.loginfo(counter)
     if counter < 20:
     	print "test:",readings
     try:
          pub.publish(readings)
          readings_toInt = map(int, readings.strip().split())
          adc0_pub.publish(readings_toInt[0])
          adc1_pub.publish(readings_toInt[1])
     except:
     	pass

     #sleep(.1) # Delay for one tenth of a second