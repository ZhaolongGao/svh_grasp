#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import UInt16
import serial

def callback(data):

    # print(data.data)
    global old_cmd
    data = data.data
    
    if data > 50 and data <= 150:
        new_cmd = '\x01\x0f\x04\x1f'
    elif data > 150 and data <=200:
        new_cmd = '\x01\x0f\x06\x1f'
    elif data > 200 and data <=300:
        new_cmd = '\x01\x0f\x08\x1f'
    elif data > 300 and data <=400:
        new_cmd = '\x01\x0f\x09\x1f'
    elif data > 400 :
        new_cmd = '\x01\x0f\x09\x1f'                        
    elif data <= 50:
        new_cmd = '\x00\x00\x00\x00'

    if new_cmd != old_cmd:
        old_cmd = new_cmd
        t.write(new_cmd)


    # n=t.write(data.data.encode('utf-8'))
    # print(n)
    # print(data.data.decode('utf-8'))
    

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('stimulator', anonymous=True)

    rospy.Subscriber("adc0_chatter", UInt16, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    global old_cmd
    old_cmd = '\x00\x00\x00\x00'
    t = serial.Serial('/dev/ttyUSB1',9600)
    print(t.portstr)
    var = 1
    #while var==1:
    #   strInput1=raw_input('enter some words:')
    #    n=t.write(strInput1.encode('utf-8'))
    #    print(n)
    #    str1=t.read(n)
    #    print(str1.decode('utf-8'))
    listener()