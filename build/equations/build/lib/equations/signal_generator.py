import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import numpy as np

class SignalGenerator(Node):
    def __init__(self):
        super().__init__('signal_generator')
        self.pub = self.create_publisher(Float64, 'force_input', 10)
        self.t = 0.0
        self.dt = 0.01
        self.timer = self.create_timer(self.dt, self.publish_signal)

    def publish_signal(self):
        force = 1.0 if self.t > 1.0 else 0.0  # degrau após 1s
        msg = Float64()
        msg.data = force
        self.pub.publish(msg)
        self.t += self.dt

def main(args=None):
    rclpy.init(args=args)
    node = SignalGenerator()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
