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

## Division Extension

As an extension, prototype implementations of quantum division algorithms are included:

- Restoring Division (iterative subtraction with restoration)
- Non-Restoring Division (optimized without restoration step)

These are input-based implementations designed to demonstrate division structure using optimized arithmetic blocks.

## Division Efficiency Comparison

A comparative analysis is included based on:

- Operation count
- Estimated circuit depth
- CX gate scaling

Result: Non-restoring division shows lower operational cost compared to restoring division.

## Project Structure

```
quantum-arithmetic-analysis/
│
├── src/               # Core circuit implementations
│   ├── full_adder.py
│   ├── metrics.py
│   ├── qft_adder.py
│   ├── ripple_adder.py
│   ├── subtractor_inverse.py
│   ├── subtractor_twos_complement.py
│   ├── quantum_restoring_division.py
│   ├── quantum_non_restoring_division.py
│
├── experiments/       # Experimental scripts
│   ├── compare_adders.py
│   ├── compare_subtractors.py
│   ├── noise_analysis.py
│   ├── compare_division.py
│
├── results/           # Generated graphs
│   ├── depth_comparison.png
│   ├── cx_comparison.png
│   ├── subtractor_depth.png
│   ├── division_advanced_comparison.png
│
├── README.md
└── requirements.txt

```

# Running Experiments

```bash
python -m experiments.compare_adders
python -m experiments.compare_subtractors
python -m experiments.noise_analysis
python -m experiments.compare_division
```
## Installation
Clone the repository and install dependencies:
```bash
pip install -r requirements.txt
```
