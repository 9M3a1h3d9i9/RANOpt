# RANOpt — Intelligent Mobile RAN Optimization

> A research-oriented framework for mobile Radio Access Network (RAN) KPI analysis, diagnosis, and optimization.

## Vision

RANOpt is designed as a modular research and engineering project for studying how data-driven methods can support mobile network optimization.

The long-term pipeline is:

```text
RAN Data
   ↓
KPI Validation & Preprocessing
   ↓
Network / Cell State
   ↓
Problem Detection
   ↓
Diagnosis
   ↓
Optimization Objective
   ↓
Candidate Actions
   ↓
AI / Reinforcement Learning
   ↓
Simulation & Evaluation
```

## Phase 1 — RAN Data & KPI Intelligence

The first phase establishes the reproducible foundation rather than claiming real operator optimization.

### Implemented in Phase 1

- Typed RAN KPI data model
- Input validation and domain checks
- Configurable KPI thresholds
- Deterministic synthetic RAN dataset generation
- CSV-oriented data loading
- Basic preprocessing utilities
- Explainable cell-health scoring
- YAML configuration
- Unit tests and integration tests
- Python package configuration
- CI-ready project structure

### KPI scope

The initial technology-neutral schema covers:

- RSRP
- RSRQ
- SINR
- Downlink throughput
- Uplink throughput
- Drop rate
- Handover success rate
- Availability

These values are intended for research and simulation. They are **not operator-specific thresholds** and must not be interpreted as measurements from a real mobile network.

## Repository Structure

```text
RANOpt/
├── configs/
│   └── default.yaml
├── data/
│   └── sample/
├── docs/
│   ├── architecture.md
│   ├── data_model.md
│   └── roadmap.md
├── examples/
│   └── phase1_demo.py
├── src/
│   └── ranopt/
│       ├── data/
│       ├── kpi/
│       ├── preprocessing/
│       └── utils/
├── tests/
│   ├── integration/
│   └── unit/
├── pyproject.toml
└── README.md
```

## Quick Start

```bash
python -m pip install -e ".[dev]"
python examples/phase1_demo.py
pytest
```

## Development Roadmap

- **Phase 1:** RAN data and KPI intelligence — current
- **Phase 2:** Monitoring, time-series analysis, and anomaly detection
- **Phase 3:** Diagnosis and optimization recommendations
- **Phase 4:** Graph-based state representation and reinforcement-learning optimization

## Research Integrity

RANOpt currently uses synthetic data and engineering assumptions. No real operator KPI improvement, production deployment, or benchmark result is claimed until experiments are actually executed and documented.

## Portfolio Role

RANOpt is the dedicated mobile-RAN optimization project in Mohammad Mahdi Shafighi's AI portfolio. It is intentionally separate from **NetSpector**, which focuses on network/RAN monitoring, and from **NeuroBottleneck**, which is maintained separately as a grant research project.

## License

MIT License.
