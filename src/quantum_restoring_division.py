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


def quantum_restoring_division(dividend, divisor):
    n = max(dividend.bit_length(), divisor.bit_length())

    q_dividend = QuantumRegister(n, 'dividend')
    q_divisor = QuantumRegister(n, 'divisor')
    q_quotient = QuantumRegister(n, 'quotient')
    c = ClassicalRegister(n, 'c')

    qc = QuantumCircuit(q_dividend, q_divisor, q_quotient, c)

    encode_number(qc, q_dividend, dividend)
    encode_number(qc, q_divisor, divisor)

    remainder = dividend

    for i in range(n):

        #step 1: subtract
        remainder -= divisor
        ripple_subtractor(qc, q_dividend, q_divisor)

        #step 2: check
        if remainder < 0:
            #step 3: restore
            remainder += divisor
            ripple_subtractor(qc, q_dividend, q_divisor)  # symbolic add

        else:
            #step 4: set quotient bit
            qc.x(q_quotient[i])

    qc.measure(q_quotient, c)
    return qc


#example
dividend = int(input("Enter dividend: "))
divisor = int(input("Enter divisor: "))
qc = quantum_restoring_division(dividend, divisor)

sim = AerSimulator()
compiled = transpile(qc, sim)
result = sim.run(compiled, shots=1024).result()

counts = result.get_counts()

print("Division Result (Quotient counts):", counts)

qc.draw('mpl')