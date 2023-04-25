#!/usr/bin/env python3

import rospy

from duckietown.dtros import DTROS, DTParam, NodeType, TopicType
from dt_class_utils import DTReminder
from duckietown_msgs.msg import BoolStamped

import RPi.GPIO as GPIO #@uncomment


class ConnectionStatusNode(DTROS):
    def __init__(self, node_name):
        super().__init__(node_name, node_type=NodeType.DRIVER)        
        # publisher
        self.connection_status_pub = rospy.Publisher("~connection_status", BoolStamped, queue_size=1)
        
    def get_connection_status(self):
        BUTTON_GPIO = 24
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(BUTTON_GPIO, GPIO.IN)
        gpio_state = GPIO.input(BUTTON_GPIO)
        connection_msg = BoolStamped()
        if gpio_state:
            connection_msg.data = True
        else:
            connection_msg.data = False
        self.connection_status_pub.publish(connection_msg)
        rospy.loginfo(f"message was {connection_msg}")
            
    def start(self):
        rate = rospy.Rate(5) # 5hz
        while not rospy.is_shutdown():
            self.get_connection_status()
            rate.sleep()


if __name__ == "__main__":
    connection_status_node = ConnectionStatusNode("connection_status")
    connection_status_node.start()
    rospy.spin()

