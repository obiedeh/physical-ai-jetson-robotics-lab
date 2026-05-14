# OpenUSD / Isaac Digital Twin Report

Date: 2026-05-14

Operator: oedeh

Machine: aimlstation, ASUSTeK COMPUTER INC. ROG G700TF, Ubuntu 24.04.4 LTS, Linux 6.17.0-23-generic, x86_64

## Environment

- GPU: NVIDIA GeForce RTX 5090, 32607 MiB VRAM
- Driver: 595.58.03; NVIDIA-SMI 580.126.09; reported CUDA runtime 13.2
- Isaac Sim version: 5.1.0 (`/home/oedeh/isaacsim/VERSION`: `5.1.0-rc.19+release.26219.9c81211b.gl`)
- Isaac Lab version: not found under `/home/oedeh`; not installed in this repo
- Python: 3.12.3
- Repo commit: d8f09ca62851523ba9a35e0b4c00cee8c91ffb0a

## Inventory Evidence

Inventory JSON:

```text
reports/inventory/linux_rtx.json
```

Commands run:

```bash
physical-ai-lab collect-inventory --target linux-rtx --output reports/inventory/linux_rtx.json
nvidia-smi --query-gpu=name,driver_version,memory.total --format=csv,noheader
python3 --version
hostnamectl
git rev-parse HEAD
```

## Scene

- USD scene path: not yet created in repo; `isaac/README.md` currently lists the factory-cell scene as planned work
- Robot assets: Yahboom robo car and Synria robotic arm references planned; no USD robot assets committed yet
- Sensors: planned camera viewpoints; no sensor USD/config committed yet
- Workcell objects: planned factory-cell objects; no workcell USD committed yet
- Lighting: not configured yet
- Physics enabled: not validated yet

## Validation

- Scene opens: not validated; no repo USD scene exists yet
- Camera renders: not validated
- Robot spawns: not validated
- Collision geometry: not validated
- Screenshot path: not captured
- Known issues: Isaac Sim is installed outside PATH at `/home/oedeh/isaacsim`; Isaac Lab is not present; CUDA toolkit `nvcc` is not on PATH; ROS 2 is not on PATH

## Synthetic Data

- Camera viewpoints: not configured yet
- Object classes: not configured yet
- Sample count: 0
- Output path: not created
- Dataset size: 0

## Robot Training

- Isaac Lab task: not created yet
- Observation space: not defined yet
- Action space: not defined yet
- Reward: not defined yet
- Training steps: 0
- Evaluation result: not run

## Business Relevance

The current Linux RTX workstation is suitable for the OpenUSD/Isaac track: the RTX 5090 and Isaac Sim 5.1.0 install are present and ready for scene bringup. The digital twin work is not yet producing risk reduction because the repo does not yet contain a USD factory-cell scene, robot assets, synthetic-data workflow, or Isaac Lab task. Once those assets are committed, the environment can reduce physical bringup risk by validating robot geometry, camera placement, collision zones, and policy behavior before running on the real Yahboom/Synria hardware.

## Next Actions

- [ ] Add a repo-local OpenUSD factory-cell scene under `isaac/usd/`
- [ ] Add Yahboom robo car and Synria arm asset references or converted USD assets
- [ ] Add an Isaac Sim smoke script that opens the scene, renders one camera frame, and writes a screenshot artifact
