from qiskit import QuantumCircuit, QuantumRegister
from qiskit.circuit.library import CDKMRippleCarryAdder

def create_ripple_adder(n):
    """
    Creates an n-bit ripple carry adder with carry-in.
    """

    cin = QuantumRegister(1, 'cin')
    a = QuantumRegister(n, 'a')
    b = QuantumRegister(n + 1, 'b')

    adder = CDKMRippleCarryAdder(n, kind='full')
    anc = QuantumRegister(adder.num_ancillas, 'anc')

    qc = QuantumCircuit(cin, a, b, anc)

    qc.append(adder, cin[:] + a[:] + b[:] + anc[:])
    qc = qc.decompose().decompose()

    # Further decompose into basic gates for accurate depth measurement
    from qiskit import transpile
    qc = transpile(qc, basis_gates=['cx', 'ccx', 'x', 'u'], optimization_level=0)

    return qc


if __name__ == "__main__":
    n = 3
    qc = create_ripple_adder(n)

    print("Ripple Adder for", n, "bits")
    print("Depth:", qc.depth())
    print("Gate Count:", qc.count_ops())