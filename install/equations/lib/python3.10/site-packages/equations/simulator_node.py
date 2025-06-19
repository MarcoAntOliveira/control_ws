import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import numpy as np

class SimulatorNode(Node):
    def __init__(self):
        super().__init__('simulator_node')
        self.declare_parameter('m', 1.0)
        self.declare_parameter('k', 10.0)
        self.declare_parameter('c', 1.0)

        self.m = self.get_parameter('m').get_parameter_value().double_value
        self.k = self.get_parameter('k').get_parameter_value().double_value
        self.c = self.get_parameter('c').get_parameter_value().double_value

        self.dt = 0.01
        self.x = 0.0
        self.v = 0.0
        self.f = 0.0

        self.sub = self.create_subscription(Float64, 'force_input', self.force_callback, 10)
        self.pub = self.create_publisher(Float64, 'position', 10)

        self.timer = self.create_timer(self.dt, self.update)

    def force_callback(self, msg):
        self.f = msg.data

    def update(self):
        # Equações diferenciais discretizadas (Euler)
        a = (self.f - self.c*self.v - self.k*self.x) / self.m
        self.v += a * self.dt
        self.x += self.v * self.dt

        msg = Float64()
        msg.data = self.x
        self.pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = SimulatorNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
