# Implement a Toffoli gate that inverts the third qubit if the first two qubits are in the state |11⟩. Simulate and visualize the behavior.

from qiskit import QuantumCircuit, Aer, transpile, execute
from qiskit.visualization import plot_bloch_multivector

# Create a quantum circuit with 3 qubits
qc = QuantumCircuit(3)

# Apply a Toffoli gate (CCX gate) to invert the third qubit if the first two qubits are in |11⟩
qc.ccx(0, 1, 2)

# Simulate the circuit and get the resulting statevector
simulator = Aer.get_backend('statevector_simulator')
compiled_circuit = transpile(qc, simulator)
job = execute(compiled_circuit, simulator)
result = job.result()
statevector = result.get_statevector(qc)

# Print the resulting statevector
print("Resulting statevector:", statevector)

# Visualize the state on a Bloch sphere for the third qubit
plot_bloch_multivector(statevector)
