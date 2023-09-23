# Build a circuit that simulates the controlled-Z gate using basic quantum gates (Hadamard, CNOT, and phase gates).

from qiskit import QuantumCircuit, Aer, transpile, execute
from qiskit.visualization import plot_bloch_multivector

# Create a quantum circuit with 2 qubits
qc = QuantumCircuit(2)

# Apply a Hadamard gate to qubit 1
qc.h(1)

# Apply a CNOT gate with qubit 1 as the control and qubit 0 as the target
qc.cx(1, 0)

# Apply a phase gate (Z gate) to qubit 0
qc.z(0)

# Apply a CNOT gate again to "undo" the previous CNOT
qc.cx(1, 0)

# Apply another Hadamard gate to qubit 1
qc.h(1)

# Simulate the circuit and get the resulting statevector
simulator = Aer.get_backend('statevector_simulator')
compiled_circuit = transpile(qc, simulator)
job = execute(compiled_circuit, simulator)
result = job.result()
statevector = result.get_statevector(qc)

# Print the resulting statevector
print("Resulting statevector:", statevector)

# Visualize the state on a Bloch sphere for both qubits
plot_bloch_multivector(statevector)
