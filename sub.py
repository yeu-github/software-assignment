#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String


def callback(data):

		if data.data[0] == "A" and data.data[-1] == "B":
			if len(data.data) == 18:
				y = [data.data[1:5], data.data[5:9], data.data[9:13], data.data[13:17]]
			elif len(data.data) == 26:
				y = [data.data[1:5], data.data[5:9], data.data[9:13], data.data[13:17],data.data[17:21], data.data[21:25]]

			for x in xrange(0, int(len(y))):
				z = int(y[x])
				if z < 280:
					z = -1 * z
					if z < -255:
						z = -255

				elif z > 1000:
					z = z - 1000
					if z > 255:
						z = 255

				y[x] = z

			if len(data.data) == 18:
				rospy.loginfo("Drive code = A  {} {} {} {} B " .format(y[0], y[1], y[2], y[3]))
			else:
				rospy.loginfo("Robotic Arm code = A  {} {} {} {} {} {} B " .format(y[0], y[1], y[2], y[3], y[4], y[5]))
				

def subs():

	rospy.init_node('listener', anonymous=True)

	rospy.Subscriber('/serial/drive', String, callback)
	rospy.Subscriber('/serial/robotic_arm', String, callback)

	rospy.spin()

if __name__ == '__main__':
	subs()
