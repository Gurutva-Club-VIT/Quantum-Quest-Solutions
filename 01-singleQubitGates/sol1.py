# Write a Qiskit program that applies a Hadamard gate to a qubit and measures it. Compare the measurement outcomes to the theoretical probabilities.

from qiskit import QuantumCircuit, transpile, assemble, Aer, execute
from qiskit.visualization import plot_histogram

# Create a quantum circuit with 1 qubit
qc = QuantumCircuit(1, 1)

# Apply a Hadamard gate to the qubit
qc.h(0)

# Measure the qubit
qc.measure(0, 0)

# Simulate the circuit on a classical computer
simulator = Aer.get_backend('qasm_simulator')
compiled_circuit = transpile(qc, simulator)
job = execute(compiled_circuit, simulator, shots=1000)
result = job.result()

# Get the measurement outcomes
counts = result.get_counts(qc)

# Calculate theoretical probabilities
theory_probs = {'0': 0.5, '1': 0.5}

# Compare measurement outcomes to theoretical probabilities
print("Measurement outcomes:", counts)
print("Theoretical probabilities:", theory_probs)

# Plot a histogram of the results
plot_histogram(counts)
