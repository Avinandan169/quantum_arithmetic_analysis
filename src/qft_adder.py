from qiskit import QuantumCircuit, QuantumRegister, transpile
from qiskit.circuit.library import DraperQFTAdder

def create_qft_adder(n):

    a = QuantumRegister(n, 'a')
    b = QuantumRegister(n, 'b')

    adder = DraperQFTAdder(n)
    qc = QuantumCircuit(a, b)

    qc.append(adder, a[:] + b[:])

    # Decompose to expose real gate structure
    qc = qc.decompose().decompose()

    qc = transpile(
        qc,
        basis_gates=['cx', 'u'],
        optimization_level=0
    )

    return qc


if __name__ == "__main__":
    n = 3
    qc = create_qft_adder(n)

    print("QFT Adder for", n, "bits")
    print("Depth:", qc.depth())
    print("Gate Count:", qc.count_ops())