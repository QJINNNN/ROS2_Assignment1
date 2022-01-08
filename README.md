# ROS2_Assignment1

## Process
* 목표는 /turtlesim 노드에 /turtle1/cmd_vel 토픽의 메시지를 전달하는 것이며, 해당 메시지의 타입은 'Twist'이다(geometry_msgs/msg/Twist)
* Twist 메시지 타입은 vector3 linear & vector3 angular 즉, 3개의 linear velocity & 3개의 angular velocity로 이루어져 있다
* 원운동의 radius, velocity, direction 정보를 Twist 메시지 타입에 그대로 적용시킬 수 없으므로, 새 패키지를 만들어 세 변수를 포함하는 새로운 메시지 타입(Input.msg)을 정의한다
* Input 메시지 타입의 토픽을 '/radius_velocity_direction'이라고 명명하고, 이 토픽을 subscribe하는 Node를 생성한다(transformer)
* transformer 노드에서는 Input 메시지 타입을 Twist 메시지 타입으로 변환시켜주고 이를 /turtle1/cmd_vel 토픽으로 publish한다
* 상기 토픽의 Twist 메시지는 최종적으로 /turtlesim 노드에 전달된다
* turtlesim_node 노드와 transformer 노드를 동시에 실행시킬 수 있는 launch 파일(assignment1_launch.launch.py)을 작성한다
* turtlesim 실행 후, 하기 코드를 통해 거북이는 사용자가 지정한 radius, velocity, direction 값을 포함하는 등속원운동을 한다. 이때 direction에서 1은 CCW, -1은 CW 방향을 의미한다

```python
ros2 topic pub --once /radius_velocity_direction assignment1_pubsub/msg/Input "{radius: VALUE, velocity: VALUE, direction: 1 or -1}"
```

## rqt_graph

![rosgraph](https://user-images.githubusercontent.com/80100520/148633855-2bb05142-693e-4861-92f6-22f133d0d794.png)
