#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
import math
from location_monitor.msg import landmarkDistance

class LandMarkMonitor(object):
	def __init__(self, pub, landmarks):
		self._pub = pub
		self._landmarks = landmarks

	def callback(self, msg):
		x = msg.pose.pose.position.x
		y = msg.pose.pose.position.y
		closest_name = None
		closest_distance = None 
		for name, x_lm, y_lm in self.landmarks:
			dist = distance(x, y, x_lm, y_lm)
			if closest_distance is None or dist < closest_distance:
				closest_name = name 
				closest_distance = dist
		rospy.loginfo('closest: {}'.format(closest_name))

def distance(x1, y1, x2, y2):
	xd = x1 - x2
	yd = y1 - y2
	return math.sqrt(xd**2 + yd**2)

def main():
	landmarks = []
	landmarks.append(("TopCube", 2.45, 0.30))
	landmarks.append(("RightCube", 1.59, -1.96))
	landmarks.append(("LeftCube", 1.38, 1.96))
	

	rospy.init_node('location_montior')
	pub = rospy.Publisher('closest_landmark', landmarkDistance)
	monitor = LandmarkMonitor(pub, landmarks)

	rospy.Subscriber("/odom", Odometry, monitor.callback)
	rospy.spin()

if __name__ == '__main__':
	main()

