# sinusoidal_publisher.py
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import math
import time

class SinPublisher(Node):
    def __init__(self):
        super().__init__('sin_publisher')
        self.publisher_ = self.create_publisher(Float64, '/position', 10)
        self.timer = self.create_timer(0.05, self.timer_callback)
        self.start_time = time.time()

    def timer_callback(self):
        elapsed = time.time() - self.start_time
        msg = Float64()
        msg.data = 0.1 * math.sin(2 * math.pi * 0.5 * elapsed)
        self.publisher_.publish(msg)

def main():
    rclpy.init()
    node = SinPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
