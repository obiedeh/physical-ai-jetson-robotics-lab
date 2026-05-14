# Linux RTX Setup

Use the Linux RTX workstation for Isaac Sim, Isaac Lab, OpenUSD, ROS 2 simulation, rendering, and robot training.

## Baseline Checks

```bash
nvidia-smi
python3 --version
git --version
```

## Python Dev Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
pytest -q
```

## Collect Inventory Evidence

```bash
bash scripts/linux_rtx/collect_inventory.sh
```

Output:

```text
reports/inventory/linux_rtx.json
```

## NVIDIA Stack Targets

Install and validate these on the RTX machine:

- NVIDIA driver with RTX GPU support
- Isaac Sim
- Isaac Lab
- OpenUSD/USD tooling
- ROS 2, if using simulation or bridge workflows
- CUDA toolkit as required by the installed Isaac stack

## Isaac/OpenUSD Track

Planned repo locations:

```text
isaac/usd/          # USD assets and scenes
isaac/scenes/       # Isaac Sim scene configs and launch notes
isaac/lab_tasks/    # Isaac Lab environments and training tasks
isaac/scripts/      # Linux RTX helper scripts
```

## Validation Goals

- open a minimal USD scene
- render a camera view
- spawn a robo car or arm placeholder
- export a screenshot or synthetic dataset sample
- run one Isaac Lab training smoke task

Start from the report template:

```text
reports/isaac/OPENUSD_TEMPLATE.md
```

## Output Artifacts To Commit

Commit code, configs, docs, and small screenshots. Do not commit large generated datasets, simulation caches, or full training runs.
