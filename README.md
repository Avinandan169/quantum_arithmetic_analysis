# Quantum Arithmetic Circuit Analysis

## Overview

This project implements and analyzes quantum arithmetic circuits using IBM Qiskit.

The study includes:

- 1-bit Quantum Full Adder (manual gate-level design)
- Ripple Carry Adder (CDKM implementation)
- QFT-based Adder (Draper Adder)
- Two’s Complement Subtractor
- Inverse Adder-based Subtractor
- Hardware-level decomposition and transpilation
- Depth and CX gate scaling analysis
- Noise modeling using depolarizing error

## Project Structure

quantum-arithmetic-analysis/
│
├── src/                # Core circuit implementations
├── experiments/        # Experimental comparison scripts
├── results/            # Generated graphs
├── notebooks/          # (Optional) Interactive demo
├── README.md
└── requirements.txt

# Running Experiments

python -m experiments.compare_adders
python -m experiments.compare_subtractors
python -m experiments.noise_analysis

## Installation

Clone the repository and install dependencies:

```bash
pip install -r requirements.txt
