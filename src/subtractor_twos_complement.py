from qiskit import QuantumCircuit, QuantumRegister, transpile
from qiskit.circuit.library import CDKMRippleCarryAdder

def create_twos_complement_subtractor(n):

    A = QuantumRegister(n, 'A')       # subtrahend
    M = QuantumRegister(n + 1, 'M')   # minuend
    cin = QuantumRegister(1, 'cin')

    adder = CDKMRippleCarryAdder(n, kind='full')
    anc = QuantumRegister(adder.num_ancillas, 'anc')

    qc = QuantumCircuit(A, M, cin, anc)

    # Step 1: Invert A
    qc.x(A)

    # Step 2: Set carry-in = 1
    qc.x(cin)

    # Step 3: Perform addition
    qc.append(adder, cin[:] + A[:] + M[:] + anc[:])

    qc = qc.decompose().decompose()

    qc = transpile(
        qc,
        basis_gates=['cx', 'ccx', 'x', 'u'],
        optimization_level=0
    )

    return qc


if __name__ == "__main__":
    n = 3
    qc = create_twos_complement_subtractor(n)

    print("Two's Complement Subtractor for", n, "bits")
    print("Depth:", qc.depth())
    print("Gate Count:", qc.count_ops())