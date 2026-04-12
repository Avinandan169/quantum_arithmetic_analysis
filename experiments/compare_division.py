import matplotlib.pyplot as plt

n_values = [2, 3, 4, 5, 6, 7]

# ----------- METRICS ------------

# Restoring Division
restoring_ops = [2*n for n in n_values]              # subtract + restore
restoring_depth = [3*n for n in n_values]            # deeper due to restore
restoring_cx = [5*n for n in n_values]               # more controlled ops

# Non-Restoring Division
nonrestoring_ops = [n for n in n_values]             # single operation per step
nonrestoring_depth = [2*n for n in n_values]         # less depth
nonrestoring_cx = [3*n for n in n_values]            # fewer CX gates


# ----------- PLOTTING ------------

plt.figure(figsize=(10, 6))

# Plot Operations
plt.plot(n_values, restoring_ops, 'o-', label='Restoring Ops')
plt.plot(n_values, nonrestoring_ops, 's-', label='Non-Restoring Ops')

# Plot Depth
plt.plot(n_values, restoring_depth, 'o--', label='Restoring Depth')
plt.plot(n_values, nonrestoring_depth, 's--', label='Non-Restoring Depth')

# Plot CX Count
plt.plot(n_values, restoring_cx, 'o:', label='Restoring CX')
plt.plot(n_values, nonrestoring_cx, 's:', label='Non-Restoring CX')

plt.xlabel("Input Size (n)")
plt.ylabel("Estimated Cost")
plt.title("Quantum Division Efficiency Comparison")

plt.legend()
plt.grid()

plt.savefig("results/division_advanced_comparison.png")
plt.show()