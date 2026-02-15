from src.subtractor_twos_complement import create_twos_complement_subtractor
from src.subtractor_inverse import create_inverse_subtractor
from src.metrics import circuit_metrics
import matplotlib.pyplot as plt

sizes = [2, 3, 4, 5]

twos_depth = []
inv_depth = []

for n in sizes:
    print("Testing n =", n)

    twos = create_twos_complement_subtractor(n)
    inv = create_inverse_subtractor(n)

    twos_metrics = circuit_metrics(twos)
    inv_metrics = circuit_metrics(inv)

    twos_depth.append(twos_metrics["depth"])
    inv_depth.append(inv_metrics["depth"])

    print("Two's complement depth:", twos_metrics["depth"])
    print("Inverse depth:", inv_metrics["depth"])
    print("-------------------")

plt.plot(sizes, twos_depth)
plt.plot(sizes, inv_depth)
plt.xlabel("Number of Qubits")
plt.ylabel("Depth")
plt.title("Subtractor Depth Comparison")
plt.legend(["Two's Complement", "Inverse"])
plt.savefig("results/subtractor_depth.png")
plt.show()