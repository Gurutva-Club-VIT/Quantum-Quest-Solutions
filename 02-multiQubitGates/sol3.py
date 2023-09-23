# Create a circuit that performs a controlled-phase gate (CPHASE) between two qubits. Observe the effect of the CPHASE gate on different input states.

from qiskit import QuantumCircuit, transpile, execute, Aer
from qiskit.visualization import plot_bloch_multivector

# Create a quantum circuit with 2 qubits
qc = QuantumCircuit(2)

# Apply a Hadamard gate to the first qubit to create a superposition state (|+⟩)
qc.h(0)

# Apply the controlled-phase gate (CPHASE) between qubit 0 and qubit 1
angle = 0.5  # You can change the phase angle here
qc.cp(angle, 0, 1)

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
