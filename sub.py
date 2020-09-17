#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String


def callback(data):

	if len(data.data) == 18:
		if data.data[0] == "A":
			if data.data[17] == "B":
				a = int(data.data[1:5])
				b = int(data.data[5:9])
				c = int(data.data[9:13])
				d = int(data.data[13:17])

				if a > 255 and a < 280:
					a = 255
				elif a > 1255 and a < 1280:
					a = 1255

				if b > 255 and b < 280:
					b = 255
				elif b > 1255 and b < 1280:
					b = 1255

				if c > 255 and c < 280:
					c = 255
				elif c > 1255 and c < 1280:
					c = 1255

				if d > 255 and d < 280:
					d = 255
				elif d > 1255 and d < 1280:
					d = 1255
				
				a1 = str(a)
				b1 = str(b)
				c1 = str(c)
				d1 = str(d)

				while len(a1) < 4:
					a1 = "O" + a1

				while len(b1) < 4:
					b1 = "O" + b1

				while len(c1) < 4:
					c1 = "O" + c1

				while len(d1) < 4:
					d1 = "O" + d1
					
				rospy.loginfo("Drive code = A  {} {} {} {} B " .format(a1, b1, c1, d1))
				
				


def callbackArm(data):

	if len(data.data) == 26:
		if data.data[0] == "A":
			if data.data[25] == "B":
				a = int(data.data[1:5])
				b = int(data.data[5:9])
				c = int(data.data[9:13])
				d = int(data.data[13:17])
				e = int(data.data[17:21])
				f = int(data.data[21:25])

				if a > 255 and a < 280:
					a = 255
				elif a > 1255 and a < 1280:
					a = 1255

				if b > 255 and b < 280:
					b = 255
				elif b > 1255 and b < 1280:
					b = 1255

				if c > 255 and c < 280:
					c = 255
				elif c > 1255 and c < 1280:
					c = 1255

				if d > 255 and d < 280:
					d = 255
				elif d > 1255 and d < 1280:
					d = 1255
				
				if e > 255 and e < 280:
					e = 255
				elif e > 1255 and e < 1280:
					e = 1255
				
				if f > 255 and f < 280:
					f = 255
				elif f > 1255 and f < 1280:
					f = 1255
				

				a1 = str(a)
				b1 = str(b)
				c1 = str(c)
				d1 = str(d)
				e1 = str(e)
				f1 = str(f)

				while len(a1) < 4:
					a1 = "O" + a1

				while len(b1) < 4:
					b1 = "O" + b1

				while len(c1) < 4:
					c1 = "O" + c1

				while len(d1) < 4:
					d1 = "O" + d1

				while len(e1) < 4:
					e1 = "O" + e1

				while len(f1) < 4:
					f1 = "O" + f1


				rospy.loginfo("Robotic Arm code = A  {} {} {} {} {} {} B " .format(a1, b1, c1, d1,e1, f1))
				#rospy.loginfo("Robotic Arm code =  " + data.data)


def subs():

	rospy.init_node('listener', anonymous=True)

	rospy.Subscriber('/serial/drive', String, callback)
	rospy.Subscriber('/serial/robotic_arm', String, callbackArm)

	rospy.spin()

if __name__ == '__main__':
	subs()
