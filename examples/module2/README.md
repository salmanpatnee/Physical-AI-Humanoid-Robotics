# Module 2 Examples: Digital Twin Simulation

This directory contains example files for Module 2: The Digital Twin (Gazebo & Unity).

## Contents

### Gazebo Examples

1. **simple_world.world** - Basic Gazebo world with physics and lighting
2. **simple_robot.urdf** - Mobile robot with camera and IMU sensors

### Unity Examples

1. **unity_scene_setup.md** - Complete guide for setting up Unity HDRP scene

## Prerequisites

### For Gazebo Examples

- ROS 2 Humble or newer
- Gazebo Classic (11.x) or Gazebo Fortress/Garden
- gazebo_ros_pkgs installed

**Installation**:
```bash
sudo apt-get update
sudo apt-get install ros-humble-gazebo-ros-pkgs
```

### For Unity Examples

- Unity Hub
- Unity Editor 2021.3 LTS or newer
- Unity Robotics Hub packages
- ROS 2 installation

## Running the Gazebo Examples

### Example 1: Simple World

Launch the basic Gazebo world:

```bash
gazebo simple_world.world
```

**What you'll see**:
- Ground plane with realistic friction
- A red box obstacle
- Directional lighting (sun)
- Physics simulation running at 1000 Hz

### Example 2: Simple Robot with Sensors

Launch Gazebo with the robot model:

```bash
# Method 1: Direct launch
gazebo simple_robot.urdf

# Method 2: Spawn robot in existing world
# Terminal 1: Launch world
gazebo simple_world.world

# Terminal 2: Spawn robot
ros2 run gazebo_ros spawn_entity.py -entity simple_robot -file simple_robot.urdf -x 0 -y 0 -z 0.5
```

**Robot Features**:
- Differential drive mobile base
- Two wheels with continuous joints
- Front-facing camera sensor (640x480 @ 30 Hz)
- IMU sensor (100 Hz update rate)

### Viewing Sensor Data

After launching the robot, view sensor topics:

```bash
# List all topics
ros2 topic list

# View camera image
ros2 run rqt_image_view rqt_image_view
# Select topic: /robot/camera/image_raw

# View IMU data
ros2 topic echo /robot/imu/data

# Plot IMU angular velocity
ros2 run rqt_plot rqt_plot /robot/imu/data/angular_velocity/x:y:z
```

### Controlling the Robot

Drive the robot using keyboard teleoperation:

```bash
# Install teleop_twist_keyboard if not already installed
sudo apt-get install ros-humble-teleop-twist-keyboard

# Run teleop
ros2 run teleop_twist_keyboard teleop_twist_keyboard

# Map to robot's cmd_vel topic
ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r /cmd_vel:=/robot/cmd_vel
```

Note: You'll need to add a differential drive plugin to the URDF for teleoperation to work. See Module 1 content for details on ROS 2 control.

## Running the Unity Examples

See [unity_scene_setup.md](unity_scene_setup.md) for complete instructions on:

1. Setting up Unity HDRP project
2. Importing robot URDF
3. Configuring lighting and materials
4. Integrating with ROS 2
5. Creating interactive scenarios

**Quick Start**:

1. Install Unity Robotics Hub packages
2. Create HDRP project
3. Import simple_robot.urdf
4. Configure ROS-TCP-Connector
5. Press Play and observe photorealistic rendering

## Modifying the Examples

### Customizing the World

Edit `simple_world.world` to:

- Change gravity: Modify `<gravity>0 0 -9.81</gravity>`
- Add more obstacles: Copy the `<model name="box_obstacle">` block
- Adjust lighting: Change `<diffuse>` and `<direction>` values
- Modify physics: Adjust `<max_step_size>` and update rates

### Customizing the Robot

Edit `simple_robot.urdf` to:

- Change robot dimensions: Modify `<box size="..."/>` values
- Add more sensors: Copy sensor blocks from Chapter 2 examples
- Adjust sensor parameters: Change resolution, update rates, FOV
- Modify noise models: Adjust `<stddev>` values for realistic simulation

### Example Modifications

**Add a LiDAR sensor**:

```xml
<link name="lidar_link">
  <sensor name="lidar" type="ray">
    <update_rate>10</update_rate>
    <ray>
      <scan>
        <horizontal>
          <samples>720</samples>
          <min_angle>-3.14159</min_angle>
          <max_angle>3.14159</max_angle>
        </horizontal>
      </scan>
      <range>
        <min>0.3</min>
        <max>10</max>
      </range>
    </ray>
    <plugin name="lidar_plugin" filename="libgazebo_ros_ray_sensor.so">
      <ros>
        <remapping>~/out:=lidar/points</remapping>
      </ros>
      <output_type>sensor_msgs/PointCloud2</output_type>
      <frame_name>lidar_link</frame_name>
    </plugin>
  </sensor>
</link>

<joint name="lidar_joint" type="fixed">
  <parent link="base_link"/>
  <child link="lidar_link"/>
  <origin xyz="0 0 0.15" rpy="0 0 0"/>
</joint>
```

**Change to lunar gravity**:

In `simple_world.world`:
```xml
<gravity>0 0 -1.62</gravity>
```

## Troubleshooting

### Gazebo Issues

**Error: "Could not find the Gazebo ros_api plugin"**
- Solution: Install gazebo_ros_pkgs
  ```bash
  sudo apt-get install ros-humble-gazebo-ros-pkgs
  ```

**Robot falls through ground**
- Solution: Check collision geometry and physics step size
- Ensure robot is spawned above ground (z > 0.5)

**Sensors not publishing**
- Solution: Check ROS 2 environment is sourced
  ```bash
  source /opt/ros/humble/setup.bash
  ```

### Unity Issues

**URDF import fails**
- Solution: Verify mesh file paths are relative
- Check all mesh files exist in specified locations

**ROS connection timeout**
- Solution: Verify ros-tcp-endpoint is running
- Check firewall allows port 10000
- Confirm ROS IP address is correct

## Learning Exercises

1. **Modify Physics**: Change gravity to simulate different planets (Mars: -3.71, Moon: -1.62)
2. **Add Sensors**: Add a depth camera or contact sensors
3. **Create Obstacles**: Build a maze environment for robot navigation
4. **Noise Tuning**: Experiment with sensor noise parameters to match real hardware
5. **Unity Scene**: Create a realistic kitchen environment for robot testing

## Additional Resources

- [Gazebo Tutorials](http://gazebosim.org/tutorials)
- [URDF Tutorials](http://wiki.ros.org/urdf/Tutorials)
- [Unity Robotics Hub](https://github.com/Unity-Technologies/Unity-Robotics-Hub)
- [ROS 2 Documentation](https://docs.ros.org/en/humble/)

## Support

For issues or questions related to these examples:
- Check Module 2 course content for detailed explanations
- Review Gazebo and ROS 2 documentation
- Post questions in the course discussion forum
