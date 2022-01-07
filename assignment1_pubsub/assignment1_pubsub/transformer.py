import rclpy
from rclpy.node import Node

from std_msgs.msg import String, Float32, Int64
from assignment1_msg.msg import Input
from geometry_msgs.msg import Twist, Vector3

class transformer(Node):

    def __init__(self):
        super().__init__('transformer')
        self.radius = 0.0
        self.velocity = 0.0
        self.direction = 0

        self.twist = None
        self.linear = None
        self.angular = None

        self.linear_x = 0.0
        self.linear_y = 0.0
        self.linear_z = 0.0
        
        self.angular_x = 0.0
        self.angular_y = 0.0
        self.angular_z = 0.0

        self.subscriber = self.create_subscription(Input, 'radius_velocity_direction', self.subscribe_msg, 10)
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

        timer_period = 1  
        self.timer = self.create_timer(timer_period, self.publish_msg)

    def subscribe_msg(self, msg):
        self.radius = msg.radius
        self.velocity = msg.velocity
        self.direction = msg.direction

    def publish_msg(self):
        self.twist = Twist()
        self.linear = Vector3()
        self.angular = Vector3()

        self.linear_x = self.velocity

        if (self.direction == 1):
            self.angular_z = self.velocity / self.radius
        elif (self.direction == -1):
            self.angular_z = -self.velocity / self.radius

        self.linear.x = self.linear_x
        self.linear.y = self.linear_y
        self.linear.z = self.linear_z

        self.angular.x = self.angular_x
        self.angular.y = self.angular_y
        self.angular.z = self.angular_z

        self.twist.linear = self.linear
        self.twist.angular = self.angular
    
        self.publisher.publish(self.twist)



def main(args=None):
    rclpy.init(args=args)

    transformation = transformer()

    rclpy.spin(transformation)

    transformation.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
