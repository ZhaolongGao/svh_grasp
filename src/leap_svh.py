#!/usr/bin/env python

## Control svh hand by Leap Motion

import rospy
from std_msgs.msg import UInt8, String
from geometry_msgs.msg import Twist, Vector3
from ros_myo.msg import MyoArm
from sensor_msgs.msg import JointState


if __name__ == '__main__':

	global armState
	global xDirState
	global handPose
	handPose = JointState()
	armState = 0
	rospy.init_node('leap_svh_controller', anonymous=True)

	svh_dbgPub = rospy.Publisher("hand_command_dbg", String, queue_size=10)
	scPub = rospy.Publisher("svh_controller/channel_targets", JointState, queue_size=10)

	# Use the calibrated Myo gestures to drive the turtle
	def drive(data):
		msg = JointState()
		# Index_Finger_Proximal   0
		# Index_Finger_Distal     1
		# Middle_Finger_Proximal  2
		# Middle_Finger_Distal    3
		# Thumb_Flexion           7
		# Thumb_Opposition        8
		msg.name = ['left_hand_Index_Finger_Proximal','left_hand_Index_Finger_Distal','left_hand_Middle_Finger_Proximal','left_hand_Middle_Finger_Distal','left_hand_Ring_Finger','left_hand_Pinky','left_hand_Finger_Spread','left_hand_Thumb_Flexion','left_hand_Thumb_Opposition']
		msg.velocity = [0,0,0,0,0,0,0,0,0] # NC
		msg.effort =   [0,0,0,0,0,0,0,0,0]   # NC
		
		# propotion from min_angle to max_angle
		efficient    = [0.0 , 0.0 , 0.0, 0.0 , 0.0 , 0.0 , 0.0 , 0.0, 0.0 ]
		
		# raw angle value from remote
		raw_value = map(int,data.data.split(' '))
		
		
		efficient[0] = min(max(raw_value[0]-8.0,0)/50.0,1)
		efficient[1] = efficient[0]

		efficient[2] = min(raw_value[1]/50.0,1)
		efficient[3] = efficient[2]

		efficient[7] = min(max(raw_value[2],0)/30.0,1)
		efficient[8] = min(raw_value[2]/30.0,1)

        #              ind_P,ind_D,mid_P,mid_D, ring,pinky,spread,thmbF,thmbO
		base_position= [0.1 , 0.1 , 0.2, 0.3 , 0.89, 0.85, 0.25, 0.1, 0.02]
		delta        = [0.5 , 0.7 , 0.4, 0.37, 0   , 0   , 0   , 0.4, 0.3 ]
		mask         = [1   , 1   , 1  , 1   , 0   , 0   , 0   , 1  , 0   ]
		msg.position = [i+eff*j*k for i,j,k,eff in zip(base_position,delta,mask,efficient)];
		rospy.loginfo(msg.position)

		# max position
		# msg.position=[0.28,0.48,0.3,0.67,0.04,0.03,0.25,0.3,0.02]

		scPub.publish(msg)

	rospy.Subscriber("leap_finger_chatter", String, drive)

	rospy.loginfo('Starting Leap Control')

	# spin() simply keeps python from exiting until this node is stopped
	rospy.spin()
