from enum import Enum
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import PoseWithCovarianceStamped
import rclpy
from rclpy.node import Node
import random

class Explore(Node):
    def __init__(self):
        super().__init__(node_name='explore')

        self.goal_pub = self.create_publisher(PoseStamped,"goal_pose", 10)
        self.current_pos_sub = self.create_subscription(PoseWithCovarianceStamped,"pose", self.current_pose_cb, 10)
        self.pose_rn = PoseWithCovarianceStamped()
        self.tmr = self.create_timer(20, self.timer_callback)

    def current_pose_cb(self, msg):
        self.pose_rn = msg

    def timer_callback(self):
        goal_pose = PoseStamped()
        goal_pose.header.frame_id = "map"
        goal_pose.header.stamp = self.get_clock().now().to_msg()
        goal_pose.pose.position.x = float(random.randint(-10,10)) + self.pose_rn.pose.pose.position.x
        goal_pose.pose.position.y = float(random.randint(-10,10)) + self.pose_rn.pose.pose.position.y
        goal_pose.pose.position.z = 0.0 
        goal_pose.pose.orientation.w = 1.0
        self.goal_pub.publish(goal_pose)

def main(args=None):
    rclpy.init(args=args)
    node = Explore()
    rclpy.spin(node)
    rclpy.shutdown()