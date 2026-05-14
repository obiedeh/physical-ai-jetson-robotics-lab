# Architecture

This project is organized around a cloud-to-sim-to-edge robotics workflow.

## Control Planes

- **Simulation plane:** OpenUSD assets, Isaac Sim scenes, Isaac Lab environments, synthetic data, and policy training.
- **Robot runtime plane:** ROS 2 nodes for robo car navigation, robotic arm control, sensor ingestion, and safety gates.
- **Edge AI plane:** Jetson Thor/Orin inference, optimization, benchmarking, and model deployment.
- **Operations plane:** telemetry, RAG over documentation and logs, operator recommendations, and AI-RAN/private 5G readiness analysis.

## Data Flow

1. OpenUSD scenes define the robot, workcell, sensors, and environment.
2. Isaac Sim/Isaac Lab generates simulation rollouts, synthetic data, and trained policies.
3. ROS 2 runs perception, localization, planning, and control on real hardware.
4. Jetson devices execute edge inference and publish telemetry.
5. The operations copilot reads telemetry, logs, and documentation to explain state and recommend next actions.

## Safety Gates

Robot actions should pass through explicit safety gates before real hardware execution:

- workspace bounds check
- collision and speed constraints
- emergency stop availability
- command source validation
- human confirmation for risky operations

## Cross-Platform Development

The core Python package supports Windows and Linux for development, testing, and portfolio review. Hardware-specific components will target Linux on Jetson and ROS 2-supported environments.
