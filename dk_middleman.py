#!/usr/bin/env python

import rospy
import time
from std_msgs.msg import String
from i2cpwm_board.msg import Servo



class donkey_driver:

	#initiate the servo control board and set the dc driver to zero
	def __init__(self):
		self.num_channels = 2
		self.is_running = False
		#Create the servoabsolute msg publisher
		self.servo_msg = Servo()
		for i in range(self.num_channels): 
			self.servo_msg.servos.append(Servo())
			self.servo_msg.servos(i).servo = i+1
		self.pubmsg = rospy.Publisher("/servos_absolute", ServoArray, queue_size=1)


	def pub(self):
		self.pubmsg.publish(self.servo_msg)

	#Turn the wheels to the left
	def left_turn(self):
		self.servo_msg.servos[1].value = 345

	#Turn the wheels to the right
	def right_turn(self):
		self.servo_msg.servos[1].value = 290

	#Center the wheels for straight movement
	def center_wheels(self):
		self.servo_msg.servos[1].value = 318
	
	#Set the servo to spin the wheels forward
	def drive_fwd(self):
		self.servo_msg.servos[0].value = 352
		time.sleep(0.2)
		self.servo_msg.servos[0].value = 349
	
	#Set the servo to spin the wheels backwards
	def drive_bwd(self):
		self.servo_msg.servos[0].value = 0
		time.sleep(0.2)
		self.servo_msg.servos[0].value = 307
		time.sleep(0.2)
		self.servo_msg.servos[0].value = 0
		time.sleep(0.2)
		self.servo_msg.servos[0].value = 307
		time.sleep(0.2)
		self.servo_msg.servos[0].value = 312

	#Stop the wheels and center/full stop
	def drive_stop(self):
		self.servo_msg.servos[0].value = 333
		self.servo_msg.servos[1].value = 318


def callback(msg):
	key_command = msg.data
	rospy.loginfo("I saw {}".format(key_command))
	if not dk.is_running:
		if key_command == 'w':
			dk.center_wheels()
			dk.drive_fwd()
		elif key_command == 'a':
			dk.left_turn()
			dk.drive_fwd()
		elif key_command == 's':
			dk.center_wheels()
			dk.drive_bwd()
		elif key_command == 'd':
			dk.right_turn()
			dk.drive_fwd()
		dk.is_running == True
	else:
		if key_command == 'w':
			dk.drive_stop()
		elif key_command == 'a':
			dk.drive_stop()
		elif key_command == 's':
			dk.drive_stop()
		elif key_command == 'd':
			dk.drive_stop()
		dk.is_running == False
	dk.pub()

def main():
	rospy.init_node("Motor_control")
	dk = donkey_driver()
	rospy.Subscriber("key_command", String, callback)
	rospy.spin()

if __name__ == '__main__':
	main()