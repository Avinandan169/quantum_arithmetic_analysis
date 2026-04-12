from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit import transpile


def encode_number(qc, qreg, number):
    """Encode classical number into quantum register"""
    for i in range(len(qreg)):
        if (number >> i) & 1:
            qc.x(qreg[i])


def ripple_subtractor(qc, a, b):
    """
    Simple reversible-style subtraction using XOR (for demo)
    NOTE: This is still simplified but logically structured
    """
    for i in range(len(a)):
        qc.cx(b[i], a[i])  # a = a XOR b (placeholder behavior)


def quantum_division(dividend, divisor):
    n = max(dividend.bit_length(), divisor.bit_length())

    # Registers
    q_dividend = QuantumRegister(n, name='dividend')
    q_divisor = QuantumRegister(n, name='divisor')
    q_quotient = QuantumRegister(n, name='quotient')
    c = ClassicalRegister(n, name='c')

    qc = QuantumCircuit(q_dividend, q_divisor, q_quotient, c)

    # Encode inputs
    encode_number(qc, q_dividend, dividend)
    encode_number(qc, q_divisor, divisor)

    # Classical-style division logic (controlled loop)
    remainder = dividend
    quotient = 0

    for i in range(n):
        if remainder >= divisor:
            remainder -= divisor
            quotient |= (1 << i)

            # Reflect subtraction in circuit (symbolic)
            ripple_subtractor(qc, q_dividend, q_divisor)

            # Mark quotient bit
            qc.x(q_quotient[i])

    # Measure quotient
    qc.measure(q_quotient, c)

    return qc


# Example
qc = quantum_division(6, 2)

sim = AerSimulator()
compiled = transpile(qc, sim)
result = sim.run(compiled, shots=1024).result()

counts = result.get_counts()

print("Division Result (Quotient counts):", counts)

qc.draw('mpl')