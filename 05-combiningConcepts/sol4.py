# Write a Qiskit program that prepares the state (|00⟩ - |11⟩) / √2 using multiple quantum gates and measures both qubits.

from qiskit import QuantumCircuit, Aer, transpile, execute
from qiskit.visualization import plot_histogram

# Create a quantum circuit with 2 qubits
qc = QuantumCircuit(2)

# Apply a Hadamard gate to the first qubit
qc.h(0)

# Apply an X gate (bit-flip) to the second qubit
qc.x(1)

# Apply a controlled-Z gate (CZ) between the qubits
qc.cz(0, 1)

# Normalize the state by dividing by sqrt(2)
qc.measure_all()

# Simulate the circuit on a classical computer
simulator = Aer.get_backend('qasm_simulator')
compiled_circuit = transpile(qc, simulator)
job = execute(compiled_circuit, simulator, shots=1000)
result = job.result()

# Get the measurement outcomes
counts = result.get_counts(qc)

# Visualize the measurement outcomes
plot_histogram(counts)
