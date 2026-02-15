from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, depolarizing_error
from qiskit import transpile
from src.ripple_adder import create_ripple_adder
from src.qft_adder import create_qft_adder

import matplotlib.pyplot as plt

n = 3

ripple = create_ripple_adder(n)
qft = create_qft_adder(n)

# Create artificial noise model
noise_model = NoiseModel()

error_1 = depolarizing_error(0.01, 1)
error_2 = depolarizing_error(0.02, 2)

noise_model.add_all_qubit_quantum_error(error_1, ['u'])
noise_model.add_all_qubit_quantum_error(error_2, ['cx'])

sim = AerSimulator(noise_model=noise_model)

ripple_t = transpile(ripple, sim)
qft_t = transpile(qft, sim)

ripple_depth = ripple.depth()
qft_depth = qft.depth()

print("Ripple depth:", ripple_depth)
print("QFT depth:", qft_depth)

print("Noise simulation executed successfully.")