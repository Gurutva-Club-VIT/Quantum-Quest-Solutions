# Create a circuit that simulates the action of a quantum coin flip: apply a Hadamard gate to a qubit and measure it to observe heads or tails.

from qiskit import QuantumCircuit, Aer, transpile, execute
from qiskit.visualization import plot_histogram

# Create a quantum circuit with 1 qubit and 1 classical bit
qc = QuantumCircuit(1, 1)

# Apply a Hadamard gate to simulate the coin flip
qc.h(0)

# Measure the qubit to observe 'heads' (|0⟩) or 'tails' (|1⟩)
qc.measure(0, 0)

# Simulate the circuit on a classical computer
simulator = Aer.get_backend('qasm_simulator')
compiled_circuit = transpile(qc, simulator)
job = execute(compiled_circuit, simulator, shots=1000)
result = job.result()

# Get the measurement outcomes
counts = result.get_counts(qc)

# Visualize the measurement outcomes
plot_histogram(counts)
