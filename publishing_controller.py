#!/usr/bin/env python

import rospy
import time
import os
#import the msg file that
from std_msgs.msg import String
#import tkinter and the such
try:
    from tkinter import *
    import tkinter as tk
    from tkinter import messagebox, filedialog
except:
    pass
try:
    from Tkinter import *
    import Tkinter as tk
    from Tkinter import messagebox, filedialog
except:
    pass


def pub_key(currentkey, depress = False):
	#initiate the node and create the publisher
	currentkey = currentkey.lower()
	rospy.init_node("key_publisher")
	pub = rospy.Publisher("key_command", String, queue_size = 10)
	#Check the key and publish the msg
	if currentkey.lower() == 'e':
		rospy.loginfo("Closing Program")
		pub.publish(currentkey.lower())
		#xset r on
		os.system('xset r on')
		dbnm.destroy()
	elif currentkey == 'w' or currentkey == 's' or currentkey == 'a' or currentkey == 'd':
		pub.publish(currentkey.lower())
		if not depress:
			rospy.loginfo("{} was pressed".format(currentkey))
		else:
			rospy.loginfo("{} was depressed".format(currentkey))

		
def key_input(event):
	key_press = event.keysym
	pub_key(key_press)

def key_stop(event):
	key_depress = event.keysym
	pub_key(key_depress, True)


if __name__ == '__main__':

	#xset r off
	os.system('xset r off')
	os.system('export ROS_MASTER_URI=http://10.0.0.66:11311')
	os.system('export ROS_IP=`hostname -I`')
	dbnm = Tk()
	dbnm.geometry("500x500")
	text = Label(dbnm, text = "wasd to move \n e to quit")
	text.config(font=("Courier", 44))
	text.pack()
	dbnm.bind('<KeyPress>', key_input)
	dbnm.bind('<KeyRelease>', key_stop)
	dbnm.mainloop()