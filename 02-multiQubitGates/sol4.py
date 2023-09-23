# Build a Qiskit program that swaps the states of two qubits using SWAP gates. Verify the correctness of the SWAP operation.

from qiskit import QuantumCircuit, Aer, transpile, execute
from qiskit.visualization import plot_bloch_multivector

# Create a quantum circuit with 2 qubits
qc = QuantumCircuit(2)

# Apply a series of SWAP gates to swap the states of the two qubits
qc.swap(0, 1)

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
