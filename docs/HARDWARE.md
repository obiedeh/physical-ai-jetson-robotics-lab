# Hardware Plan

## Target Hardware

- NVIDIA Jetson Thor
- NVIDIA Jetson Orin GX / Orin-class edge device
- Yahboom Orin NX 8GB ROS 2 robot car with mecanum wheels, display, and 6DOF arm
- robo car platform
- Synria AI Robotic Arm Kit, 6DOF, 650 mm reach, 1 kg payload
- Synria C10 wrist camera
- cameras
- optional IMU, wheel encoders, and LiDAR

## Synria AI Robotic Arm

Primary manipulation hardware:

- 6 degrees of freedom
- 650 mm reach
- 1 kg payload
- LeRobot / ALOHA-compatible learning workflows
- ROS 1 / ROS 2 support
- MoveIt / MoveIt 2 support
- Synria C10 wrist camera for eye-in-hand perception

Initial integration goals:

1. Verify vendor SDK, ROS 2 packages, URDF, meshes, and MoveIt configuration.
2. Bring up the C10 camera on Windows and Linux as a plain USB camera.
3. Bring up the C10 camera in ROS 2 on Linux.
4. Validate mock MoveIt planning before enabling real hardware motion.
5. Record safe joint limits, payload limits, workspace bounds, and emergency-stop procedure.
6. Build an OpenUSD/Isaac Sim representation for sim-first task development.

## Yahboom Orin NX ROS 2 Robot Car

Primary mobile manipulation hardware:

- Jetson Orin NX 8GB compute target
- ROS 2 robot platform
- mecanum wheel omnidirectional chassis
- 6DOF arm configuration
- display-equipped version
- multimodal AI large model support
- AI voice interaction
- vision recognition

Initial integration goals:

1. Confirm exact model line, firmware image, ROS 2 distribution, and Yahboom tutorial package.
2. Record JetPack, Ubuntu, ROS 2, CUDA, and TensorRT versions from the robot.
3. Validate base teleoperation before autonomous navigation.
4. Validate camera topics, display, microphone, speaker, and arm topics.
5. Bring up SLAM in a controlled indoor test area.
6. Add mecanum-specific odometry, calibration, and drift notes.
7. Build an OpenUSD/Isaac digital twin of the mobile base and arm.
8. Benchmark on-device vision and voice interaction workloads.

## Jetson Setup Checklist

1. Install the supported JetPack version for the target board.
2. Verify CUDA, TensorRT, and Python runtime availability.
3. Confirm camera access through CSI, USB, or GStreamer.
4. Install ROS 2 distribution compatible with the Jetson OS image.
5. Configure a dedicated ROS domain ID for lab experiments.
6. Run thermal, power, and inference smoke tests before robot integration.

## Real Robot Bring-Up Checklist

1. Validate manual control with wheels or arm motors disabled where possible.
2. Confirm sensor timestamps and coordinate frames.
3. Record baseline telemetry at idle and under load.
4. Run simulation-only tests before real-world autonomous actions.
5. Enable emergency stop and operator override.
