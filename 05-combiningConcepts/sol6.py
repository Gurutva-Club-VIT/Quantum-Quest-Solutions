# Build a Qiskit circuit that generates a random bit by applying a Hadamard gate to a qubit and measuring it.

from qiskit import QuantumCircuit, Aer, transpile, execute
import random

# Create a quantum circuit with 1 qubit and 1 classical bit
qc = QuantumCircuit(1, 1)

# Apply a Hadamard gate to simulate the coin flip
qc.h(0)

# Measure the qubit to observe '0' or '1'
qc.measure(0, 0)

# Simulate the circuit on a classical computer
simulator = Aer.get_backend('qasm_simulator')
compiled_circuit = transpile(qc, simulator)
job = execute(compiled_circuit, simulator, shots=1)
result = job.result()

# Get the measurement outcome
counts = result.get_counts(qc)
random_bit = int(list(counts.keys())[0])

# Display the random bit
print("Random bit:", random_bit)
