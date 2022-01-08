# ROS2_Assignment1

## Process
* 목표는 /turtlesim 노드에 /turtle1/cmd_vel 토픽의 메시지를 전달하는 것이며, 해당 메시지의 타입은 'Twist'이다(geometry_msgs/msg/Twist)
* Twist 메시지 타입은 vector3 linear & vector3 angular 즉, 3개의 linear velocity & 3개의 angular velocity로 이루어져 있다
* 원운동의 radius, velocity, direction 정보를 Twist 메시지 타입에 그대로 적용시킬 수 없으므로, 새 패키지를 만들어 세 변수를 포함하는 새로운 메시지 타입(Input.msg)을 정의한다
* Input 메시지 타입의 토픽을 'radius_velocity_direction'이라고 명명하고, 이 토픽을 subscribe하는 Node를 생성한다(transformer)
* transformer 노드에서는 Input 메시지 타입을 Twist 메시지 타입으로 변환시켜주고 이를 /turtle1/cmd_vel 토픽으로 publish한다
* 상기 토픽의 Twist 메시지는 최종적으로 /turtlesim 노드에 전달되어 거북이가 등속 원운동을 하게 된다

## 
