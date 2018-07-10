#!/usr/bin/env python
# Communicate with Leap in Windows (remote) via UDP
import rospy
import socket, sys
from std_msgs.msg import String

# initial ROS publisher
pub = rospy.Publisher('leap_finger_chatter', String, queue_size = 1000)
rospy.init_node('leap_finger_publisher', anonymous=True)

# create udp socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print 'Failed to create socket'
    sys.exit()
# bind socket to local ip&port
ip_addr = "192.168.56.2"
udp_port = 8012
s.bind((ip_addr,udp_port))

rospy.loginfo("start receiving...")
rospy.loginfo(ip_addr)
rospy.loginfo(udp_port)

# receive data
while True:
    data, addr = s.recvfrom(1024)
    pub.publish(data)
    rospy.loginfo(data)