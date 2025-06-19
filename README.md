## control and simulation of flight
this repository is dedicated to control and simulation of quadrirotor using robot operating system (ROS)


### Controller manager
Controller Manager is the main component in the ros2_control framework. It manages lifecycle of controllers, access to the hardware interfaces and offers services to the ROS-world.

#### Determinism
For best performance when controlling hardware you want the controller manager to have as little jitter as possible in the main control loop. The normal linux kernel is optimized for computational throughput and therefore is not well suited for hardware control. The two easiest kernel options are the Real-time Ubuntu 22.04 LTS Beta or linux-image-rt-amd64 on Debian Bullseye.

If you have a realtime kernel installed, the main thread of Controller Manager attempts to configure SCHED_FIFO with a priority of 50. By default, the user does not have permission to set such a high priority. To give the user such permissions, add a group named realtime and add the user controlling your robot to this group:

## Main Repository
[git repository](https://github.com/ros-controls)

### Chaining controllers
[Example](https://github.com/ros-controls/roadmap/blob/master/design_drafts/controller_chaining.md#example-2)

### Cascade Control

[Implementation in ros](https://github.com/ros-controls/roadmap/blob/master/design_drafts/cascade_control.md)

## ros commands
´´´bash
source install/setup.bash
source /opt/ros/humble/setup.bash
ros2 pkg create equations --build-type ament_python --dependencies rclpy

pip3 list|grep setuptools
pip3 install setuptools==58.2.0
´´´

´´´bash
ros2 run equations simulator_node
ros2 run equations signal_node
/opt/ros/humble/lib/rqt_plot/rqt_plot ./position/data
ros2 topic pub /force_input std_msgs/msg/Float64 '{data: 5.0}' --rate 10
ros2 topic echo /position
´´´
