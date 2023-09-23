# Build a circuit that prepares a qubit in the state |0⟩ and then applies an S gate. Measure the qubit and compare results with theoretical predictions.

from qiskit import QuantumCircuit, Aer, transpile, execute
from qiskit.visualization import plot_histogram

# Create a quantum circuit with 1 qubit
qc = QuantumCircuit(1, 1)

# Prepare the qubit in the |0⟩ state (this is the default state)

# Apply an S gate to the qubit
qc.s(0)

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
theory_probs = {'0': 1, '1': 0}  # The S gate doesn't change the |0⟩ state.

# Compare measurement outcomes to theoretical probabilities
print("Measurement outcomes:", counts)
print("Theoretical probabilities:", theory_probs)

# Plot a histogram of the results
plot_histogram(counts)
