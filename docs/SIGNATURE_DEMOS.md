# Signature Demos

These demos define what makes the repository stand out. Each one should produce code, evidence, and a report.

Use this template for polished demo writeups:

```text
reports/SIGNATURE_DEMO_TEMPLATE.md
```

## Demo 1: Yahboom Mobile Manipulation Bring-Up

Goal:

Prove the Yahboom Orin NX robot car is a working mobile robotics platform with ROS 2 topics, camera streams, mecanum base control, and Jetson inventory evidence.

Evidence:

- inventory JSON
- ROS topic list
- camera screenshot
- teleoperation notes
- mecanum calibration table
- first SLAM map or localization notes

Business use case:

Smart-factory mobile robot navigation and inspection.

## Demo 2: Synria Eye-In-Hand Manipulation

Goal:

Prove the Synria 6DOF arm and C10 wrist camera can support safe manipulation, visual calibration, and MoveIt 2 planning.

Evidence:

- inventory JSON
- camera stream screenshot
- URDF/MoveIt planning screenshot
- joint-state proof
- first safe motion notes
- eye-in-hand calibration notes

Business use case:

Small workcell inspection, sorting, and assistive manipulation.

## Demo 3: OpenUSD Digital Twin v0

Goal:

Build a Linux RTX OpenUSD/Isaac scene that mirrors the real lab: Yahboom mobile base, Synria arm, camera viewpoints, workcell objects, and collision zones.

Evidence:

- USD scene
- rendered screenshots
- camera viewpoint images
- synthetic data sample
- scene validation report

Business use case:

Reduce real robot risk by validating scenes, reachability, camera views, and robot tasks in simulation.

## Demo 4: Edge AI Runtime Benchmark

Goal:

Compare on-device inference behavior across available targets, especially Jetson Orin NX and Jetson Thor.

Evidence:

- model/runtime used
- latency average and p95
- FPS
- memory usage
- power and thermal notes
- CPU/GPU utilization

Business use case:

Choose the right edge deployment target for robotics perception and control workloads.

## Demo 5: Robot Operations Copilot

Goal:

Build an agentic RAG workflow that reads robot telemetry, ROS logs, manuals, and bring-up reports, then produces safety-bounded operator recommendations.

Evidence:

- document ingestion
- telemetry summary
- root-cause explanation
- recommended action with safety gates
- evaluation examples

Business use case:

Reduce robot downtime and improve operator response in industrial environments.

## Demo 6: AI-RAN Robotics Readiness

Goal:

Show how private 5G / AI-RAN latency and congestion affect mobile robot task reliability.

Evidence:

- simulated or measured network latency
- task degradation model
- workload placement recommendation
- forecast or threshold alert

Business use case:

Robotics fleet uptime in AI-native wireless smart factories.
