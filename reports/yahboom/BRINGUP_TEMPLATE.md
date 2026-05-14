# Yahboom Orin NX Robot Car Bring-Up Report

Date:

Operator:

Location:

## Hardware

- Robot model:
- Jetson model:
- RAM:
- Display:
- Camera/depth sensors:
- LiDAR:
- Arm attached:
- Battery/power notes:

## Software

- Ubuntu:
- JetPack:
- CUDA:
- TensorRT:
- ROS 2 distro:
- Yahboom image/tutorial version:
- Repo commit:

## Inventory Evidence

Inventory JSON:

```text
reports/inventory/<file>.json
```

Commands run:

```bash
physical-ai-lab collect-inventory --target jetson-orin --output reports/inventory/yahboom_orin_nx.json
```

## ROS Topic Inventory

Paste or link the topic list:

```text
ros2 topic list
```

Key topics:

- Base command:
- Odometry:
- Camera:
- Arm joint states:
- Voice input:
- Display/UI:

## Teleoperation Test

- Base moved forward/back:
- Base strafed left/right:
- Base rotated:
- Emergency stop tested:
- Notes:

## Mecanum Calibration

- Commanded distance:
- Measured distance:
- Commanded rotation:
- Measured rotation:
- Drift observed:
- Speed limits used:

## Camera / Vision Test

- Camera topic:
- Resolution:
- FPS:
- Example screenshot:
- Detection model used:
- Latency:

## SLAM / Navigation

- SLAM package:
- Map saved:
- Localization quality:
- Obstacle avoidance:
- CPU/GPU load:
- Failure cases:

## Mobile Manipulation

- Arm enabled:
- Base-to-arm frame validated:
- First task:
- Success count:
- Failure count:
- Safety notes:

## Business Relevance

Explain what this test proves for smart factories, warehouses, inspection, or embodied AI.

## Next Actions

- [ ] 
- [ ] 
- [ ] 
