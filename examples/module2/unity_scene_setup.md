# Unity Scene Setup Guide for Module 2

This guide explains how to set up the example Unity scene for high-fidelity robot rendering and interaction.

## Prerequisites

- Unity Hub installed
- Unity Editor 2021.3 LTS or newer
- Unity Robotics Hub packages installed

## Scene Components

### 1. HDRP Indoor Environment Scene

**Scene Name**: `HumanoidRoboticsInteraction.unity`

**Assets Required**:
- Unity HDRP template
- Unity Robotics Hub (URDF Importer, ROS-TCP-Connector)
- Optional: Free indoor furniture assets from Unity Asset Store

### 2. Scene Hierarchy

```
HumanoidRoboticsInteraction
├── Lighting
│   ├── Directional Light (Sun through window)
│   ├── Point Light 1 (Ceiling lamp)
│   ├── Point Light 2 (Table lamp)
│   └── HDRI Sky
├── Environment
│   ├── Floor
│   ├── Walls
│   ├── Ceiling
│   ├── Window
│   └── Furniture
│       ├── Table
│       ├── Chair
│       └── Couch
├── Robot
│   ├── Base Link (with ArticulationBody)
│   ├── Torso (with ArticulationBody)
│   ├── Head (with ArticulationBody)
│   ├── Left Arm (with ArticulationBody chain)
│   ├── Right Arm (with ArticulationBody chain)
│   ├── Left Leg (with ArticulationBody chain)
│   └── Right Leg (with ArticulationBody chain)
├── Interactive Objects
│   ├── Cup (Rigidbody + GraspableObject script)
│   ├── Book (Rigidbody + GraspableObject script)
│   └── Phone (Rigidbody + GraspableObject script)
├── Cameras
│   ├── Main Camera (Third-person view)
│   ├── Robot POV Camera (First-person from robot)
│   └── Top-down Camera (Overhead view)
└── Post-Processing
    └── Global Volume (with HDRP effects)
```

### 3. Lighting Configuration

**Directional Light (Sun)**:
- Position: (0, 10, -10)
- Rotation: (50, -30, 0)
- Intensity: 50,000 lux
- Color Temperature: 5500K (daylight)

**Point Light 1 (Ceiling)**:
- Position: (0, 3, 0)
- Intensity: 1000 lumens
- Color Temperature: 3000K (warm white)
- Range: 5m

**Point Light 2 (Table Lamp)**:
- Position: (2, 1, 2)
- Intensity: 500 lumens
- Color Temperature: 2700K (soft warm)
- Range: 3m

### 4. Material Setup

**Floor Material (HDRP/Lit)**:
- Base Color: Wood texture
- Metallic: 0.0
- Smoothness: 0.3
- Normal Map: Wood grain

**Robot Material (HDRP/Lit)**:
- Base Color: Metallic gray
- Metallic: 0.9
- Smoothness: 0.8
- Emission: Off

**Interactive Objects**:
- Use physically-based materials
- Cup: Ceramic (white, smoothness 0.6)
- Book: Matte paper (smoothness 0.1)
- Phone: Glossy plastic (smoothness 0.9)

### 5. Post-Processing Effects

**Global Volume Settings**:

```csharp
// Exposure
Exposure Mode: Fixed
Compensation: 0

// Bloom
Intensity: 0.2
Threshold: 1.0
Scatter: 0.7

// Ambient Occlusion
Intensity: 0.5
Radius: 1.0
Quality: High

// Depth of Field (optional)
Focus Distance: 5.0
Aperture: 5.6

// Color Grading
Temperature: +5 (warm indoor tone)
Tint: 0
Saturation: 110
Contrast: 105
```

### 6. Robot Setup (URDF Import)

**Step 1**: Import URDF
1. Copy robot URDF folder to `Assets/Robots/`
2. Robotics → Import URDF
3. Select robot.urdf file

**Step 2**: Configure ArticulationBody
- All joints should have ArticulationBody components
- Set joint limits matching URDF
- Configure stiffness and damping for realistic motion

**Step 3**: Add ROS Integration
- Attach `JointStateSubscriber.cs` to robot root
- Configure ROS-TCP-Connector settings
- Set ROS IP and Port

### 7. Interactive Object Scripts

**GraspableObject.cs** (attach to graspable objects):

```csharp
using UnityEngine;

public class GraspableObject : MonoBehaviour
{
    private Rigidbody rb;
    private bool isGrasped = false;
    private Transform gripper;

    void Start()
    {
        rb = GetComponent<Rigidbody>();
    }

    public void Grasp(Transform gripperTransform)
    {
        isGrasped = true;
        gripper = gripperTransform;
        rb.isKinematic = true;
    }

    public void Release()
    {
        isGrasped = false;
        rb.isKinematic = false;
    }

    void Update()
    {
        if (isGrasped && gripper != null)
        {
            transform.position = gripper.position;
            transform.rotation = gripper.rotation;
        }
    }
}
```

### 8. Camera Setup

**Main Camera**:
- Position: (-3, 2, -3)
- Rotation: (15, 45, 0)
- FOV: 60°
- Clear Flags: Skybox

**Robot POV Camera**:
- Parent: Robot Head link
- Local Position: (0, 0, 0.1)
- Local Rotation: (0, 0, 0)
- FOV: 90°

### 9. ROS-TCP Integration

**ROS Settings** (Robotics → ROS Settings):
- ROS IP Address: 127.0.0.1 (or your ROS machine IP)
- ROS Port: 10000
- Protocol: ROS2

**Required ROS Packages** (on Linux side):
```bash
sudo apt-get install ros-humble-ros-tcp-endpoint
```

**Launch ROS Endpoint**:
```bash
ros2 run ros_tcp_endpoint default_server_endpoint --ros-args -p ROS_IP:=0.0.0.0
```

## Running the Scene

1. **Start ROS Endpoint** (on ROS machine)
2. **Open Unity Scene** (`HumanoidRoboticsInteraction.unity`)
3. **Press Play** in Unity Editor
4. **Publish Joint States** from ROS:
   ```bash
   ros2 topic pub /joint_states sensor_msgs/JointState "{...}"
   ```
5. **Observe** robot moving in Unity with realistic lighting and materials

## Expected Result

You should see:
- Photorealistic indoor environment with soft lighting
- Humanoid robot with metallic materials responding to light
- Interactive objects (cup, book, phone) on surfaces
- Real-time synchronization with ROS joint states
- Realistic shadows, reflections, and ambient occlusion

## Troubleshooting

**Robot not appearing**:
- Check URDF import logs
- Verify mesh file paths in URDF
- Ensure all materials are assigned

**ROS connection failing**:
- Verify ROS IP address and port
- Check firewall settings
- Ensure ros-tcp-endpoint is running

**Poor visual quality**:
- Confirm HDRP is enabled
- Check Global Volume settings
- Verify GPU supports HDRP (GTX 1060 or better recommended)

## References

- [Unity Robotics Hub Documentation](https://github.com/Unity-Technologies/Unity-Robotics-Hub)
- [HDRP Documentation](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest)
- [Unity Learn: HDRP Lighting](https://learn.unity.com/tutorial/introduction-to-lighting-and-rendering)
