#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import UInt16
import serial

if rospy.has_param('serial_device'):
	dev_name = rospy.get_param('serial_device', '/dev/ttyACM1')
else:
	dev_name = '/dev/ttyACM1'

ser = serial.Serial(dev_name, 115200, timeout=0.5) # Establish the connection on a specific port

counter = 0 # Below 32 everything in ASCII is gibberish


pub = rospy.Publisher('sensor_chatter', String, queue_size = 1000)
adc0_pub = rospy.Publisher("adc0_chatter", UInt16, queue_size = 100)
rospy.init_node('sensor_publisher', anonymous=True)

rospy.loginfo("start reading")
ser.write('a\n')

while True:
     counter +=1
     #ser.write('a') # Convert the decimal number to ASCII then send it to the Arduino
     readings = ser.readline() # Read the newest output from the Arduino
     #rospy.loginfo(counter)
     if counter < 20:
     	print "test:",readings
     try:
     	pub.publish(readings)
     	adc0_pub.publish(int(readings.strip()))
     except:
     	pass

     #sleep(.1) # Delay for one tenth of a second