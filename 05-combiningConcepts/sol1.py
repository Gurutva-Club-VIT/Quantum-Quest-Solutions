# Create a Qiskit program that prepares the state (|00⟩ + |01⟩ + |10⟩ + |11⟩) / 2 using Hadamard and controlled gates.

from qiskit import QuantumCircuit, Aer, transpile, assemble, execute

# Create a quantum circuit with 2 qubits
qc = QuantumCircuit(2)

# Apply Hadamard gates to both qubits
qc.h(0)
qc.h(1)

# Apply controlled-X (CNOT) gates to create the desired state
qc.cx(0, 1)

# Simulate the circuit and get the resulting statevector
simulator = Aer.get_backend('statevector_simulator')
compiled_circuit = transpile(qc, simulator)
job = execute(compiled_circuit, simulator)
result = job.result()
statevector = result.get_statevector(qc)

# Print the resulting statevector
print("Resulting statevector:", statevector)
