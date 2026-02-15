from qiskit import QuantumCircuit

def create_full_adder():
    """
    1-bit quantum full adder.
    
    Qubit layout:
    0 -> A
    1 -> B
    2 -> Cin
    3 -> Sum
    4 -> Cout
    """

    qc = QuantumCircuit(5)

    # Example input: A=1, B=1, Cin=0
    qc.x(0)
    qc.x(1)

    # Sum = A XOR B XOR Cin
    qc.cx(0, 3)
    qc.cx(1, 3)
    qc.cx(2, 3)

    # Carry-out using Toffoli gates
    qc.ccx(0, 1, 4)
    qc.ccx(0, 2, 4)
    qc.ccx(1, 2, 4)

    return qc


if __name__ == "__main__":
    qc = create_full_adder()

    print("Circuit Depth:", qc.depth())
    print("Gate Count:", qc.count_ops())

    print(qc.draw())