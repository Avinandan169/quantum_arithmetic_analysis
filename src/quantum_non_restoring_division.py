from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit import transpile


def encode_number(qc, qreg, number):
    for i in range(len(qreg)):
        if (number >> i) & 1:
            qc.x(qreg[i])


def apply_operation(qc, target, control, operation="sub"):
    
    #placeholder for add/sub operation
    
    for i in range(len(target)):
        qc.cx(control[i], target[i])  # symbolic (XOR-based)


def quantum_non_restoring_division(dividend, divisor):
    n = max(dividend.bit_length(), divisor.bit_length())

    #Registers
    q_dividend = QuantumRegister(n, 'dividend')
    q_divisor = QuantumRegister(n, 'divisor')
    q_quotient = QuantumRegister(n, 'quotient')
    c = ClassicalRegister(n, 'c')

    qc = QuantumCircuit(q_dividend, q_divisor, q_quotient, c)

    #Encode inputs
    encode_number(qc, q_dividend, dividend)
    encode_number(qc, q_divisor, divisor)

    remainder = dividend
    quotient = 0

    for i in range(n):

        if remainder >= 0:
            remainder -= divisor
            quotient |= (1 << i)

            apply_operation(qc, q_dividend, q_divisor, "sub")
            qc.x(q_quotient[i])

        else:
            remainder += divisor

            apply_operation(qc, q_dividend, q_divisor, "add")

  #non restoring logic
    if remainder < 0:
        remainder += divisor

    # Measure quotient
    qc.measure(q_quotient, c)

    return qc


dividend = int(input("Enter dividend: "))
divisor = int(input("Enter divisor: "))

qc = quantum_non_restoring_division(dividend, divisor)

sim = AerSimulator()
compiled = transpile(qc, sim)
result = sim.run(compiled, shots=1024).result()

counts = result.get_counts()

print("Quotient result:", counts)

qc.draw('mpl')