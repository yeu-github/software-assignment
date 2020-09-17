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
				
				
				if a < 256:
					a = -1 * a
				else:
					a = a - 1000

				if b < 256:
					b = -1 * b
				else:
					b = b - 1000

				if c < 256:
					c = -1 * c
				else:
					c = c - 1000

				if d < 256:
					d = -1 * d
				else:
					d = d - 1000
					
				rospy.loginfo("Drive code = A  {} {} {} {} B " .format(a, b, c, d))
				
				


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
				

				
				if a < 256:
					a = -1 * a
				else:
					a = a - 1000

				if b < 256:
					b = -1 * b
				else:
					b = b - 1000

				if c < 256:
					c = -1 * c
				else:
					c = c - 1000

				if d < 256:
					d = -1 * d
				else:
					d = d - 1000

				if e < 256:
					e = -1 * e
				else:
					e = e - 1000

				if f < 256:
					f = -1 * f
				else:
					f = f - 1000


				rospy.loginfo("Robotic Arm code = A  {} {} {} {} {} {} B " .format(a, b, c, d, e, f))
				#rospy.loginfo("Robotic Arm code =  " + data.data)


def subs():

	rospy.init_node('listener', anonymous=True)

	rospy.Subscriber('/serial/drive', String, callback)
	rospy.Subscriber('/serial/robotic_arm', String, callbackArm)

	rospy.spin()

if __name__ == '__main__':
	subs()
