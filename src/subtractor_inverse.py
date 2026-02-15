from qiskit import QuantumCircuit, QuantumRegister, transpile
from qiskit.circuit.library import CDKMRippleCarryAdder

def create_inverse_subtractor(n):

    cin = QuantumRegister(1, 'cin')
    a = QuantumRegister(n, 'a')
    b = QuantumRegister(n + 1, 'b')

    adder = CDKMRippleCarryAdder(n, kind='full')
    anc = QuantumRegister(adder.num_ancillas, 'anc')

    qc = QuantumCircuit(cin, a, b, anc)

    qc.append(adder.inverse(), cin[:] + a[:] + b[:] + anc[:])

    qc = qc.decompose().decompose()

    qc = transpile(
        qc,
        basis_gates=['cx', 'ccx', 'x', 'u'],
        optimization_level=0
    )

    return qc


if __name__ == "__main__":
    n = 3
    qc = create_inverse_subtractor(n)

    print("Inverse Subtractor for", n, "bits")
    print("Depth:", qc.depth())
    print("Gate Count:", qc.count_ops())