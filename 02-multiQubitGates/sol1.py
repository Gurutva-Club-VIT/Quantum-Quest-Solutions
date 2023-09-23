# Design a Qiskit circuit that entangles two qubits using a CNOT gate. Measure both qubits and analyze the correlation between their measurement outcomes.

from qiskit import QuantumCircuit, Aer, transpile, assemble, execute
from qiskit.visualization import plot_histogram

# Create a quantum circuit with 2 qubits
qc = QuantumCircuit(2, 2)

# Apply a CNOT gate to entangle the qubits (Qubit 0 as control and Qubit 1 as target)
qc.cx(0, 1)

# Measure both qubits
qc.measure([0, 1], [0, 1])

# Simulate the circuit on a classical computer
simulator = Aer.get_backend('qasm_simulator')
compiled_circuit = transpile(qc, simulator)
job = execute(compiled_circuit, simulator, shots=1000)
result = job.result()

# Get the measurement outcomes
counts = result.get_counts(qc)

# Analyze the correlation between the measurement outcomes
print("Measurement outcomes:", counts)
