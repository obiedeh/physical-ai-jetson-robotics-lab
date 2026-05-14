# Jetson Deployment

Use Jetson Thor and Jetson Orin for real robot deployment and edge AI benchmarks.

## Target Roles

Jetson Thor:

- heavier physical AI reasoning workloads
- multi-camera perception
- VLM/LLM experiments where practical
- higher-throughput TensorRT benchmarks

Jetson Orin:

- robo car runtime
- Yahboom Orin NX robot car runtime
- robotic arm control
- SLAM/navigation
- camera inference
- baseline edge deployment comparisons

## Baseline Checks

```bash
uname -a
nvidia-smi || true
tegrastats
python3 --version
```

## Collect Inventory Evidence

```bash
bash scripts/jetson/collect_inventory.sh jetson-orin reports/inventory/yahboom_orin_nx.json
```

For Jetson Thor:

```bash
bash scripts/jetson/collect_inventory.sh jetson-thor reports/inventory/jetson_thor.json
```

## Setup Outline

1. Install the supported JetPack version for the board.
2. Verify CUDA, TensorRT, and camera access.
3. Install ROS 2 for the Jetson OS image.
4. Clone this repo.
5. Create a Python environment for non-ROS utilities.
6. Run the CLI telemetry smoke test.
7. Bring up sensors before enabling autonomous control.

## Safety Checklist

- emergency stop tested
- robot lifted or wheels disabled for first motor tests
- arm workspace cleared
- speed limits configured
- operator override available
- commands logged with timestamps

## Benchmark Reports

Each Jetson experiment should record:

- device model
- JetPack version
- model/runtime used
- average latency
- p95 latency
- FPS
- memory usage
- power/thermal notes
- sensor configuration
