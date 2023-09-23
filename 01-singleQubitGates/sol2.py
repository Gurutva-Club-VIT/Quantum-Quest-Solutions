# Create a Qiskit circuit that applies a Pauli X gate to a qubit and measures it. Observe the resulting state.

from qiskit import QuantumCircuit, Aer, transpile, execute
from qiskit.visualization import plot_bloch_multivector

# Create a quantum circuit with 1 qubit
qc = QuantumCircuit(1)

# Apply a Pauli X gate to the qubit
qc.x(0)

# Simulate the circuit and get the resulting statevector
simulator = Aer.get_backend('statevector_simulator')
compiled_circuit = transpile(qc, simulator)
job = execute(compiled_circuit, simulator)
result = job.result()
statevector = result.get_statevector(qc)

# Print the statevector
print("Resulting statevector:", statevector)

# Visualize the state on a Bloch sphere
plot_bloch_multivector(statevector)
