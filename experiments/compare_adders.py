import matplotlib.pyplot as plt
from src.ripple_adder import create_ripple_adder
from src.qft_adder import create_qft_adder

sizes = [2, 3, 4, 5]

ripple_depth = []
qft_depth = []

ripple_cx = []
qft_cx = []

for n in sizes:
    print("Running for n =", n)

    ripple = create_ripple_adder(n)
    qft = create_qft_adder(n)

    ripple_depth.append(ripple.depth())
    qft_depth.append(qft.depth())

    ripple_cx.append(ripple.count_ops().get('cx', 0))
    qft_cx.append(qft.count_ops().get('cx', 0))

    print("Ripple depth:", ripple.depth())
    print("QFT depth:", qft.depth())
    print("Ripple CX:", ripple.count_ops().get('cx', 0))
    print("QFT CX:", qft.count_ops().get('cx', 0))
    print("-----------------------")

# Depth Graph
plt.figure()
plt.plot(sizes, ripple_depth)
plt.plot(sizes, qft_depth)
plt.xlabel("Number of Qubits (n)")
plt.ylabel("Circuit Depth")
plt.title("Ripple vs QFT Depth Comparison")
plt.legend(["Ripple", "QFT"])
plt.savefig("results/depth_comparison.png")

# CX Graph
plt.figure()
plt.plot(sizes, ripple_cx)
plt.plot(sizes, qft_cx)
plt.xlabel("Number of Qubits (n)")
plt.ylabel("CX Gate Count")
plt.title("Ripple vs QFT CX Count Comparison")
plt.legend(["Ripple", "QFT"])
plt.savefig("results/cx_comparison.png")

plt.show()