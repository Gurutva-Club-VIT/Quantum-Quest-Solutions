# Simulate the quantum teleportation protocol using Qiskit. Design a circuit that transfers the state of one qubit to another using entanglement and Bell measurement.

from qiskit import QuantumCircuit, Aer, transpile, assemble, execute
from qiskit.visualization import plot_histogram

# Create a quantum circuit with 3 qubits: Alice's qubit (q0), Bell pair qubit (q1 and q2)
qc = QuantumCircuit(3, 1)

# Create entanglement between q1 and q2 (Bell pair preparation)
qc.h(1)
qc.cx(1, 2)

# Prepare the state to be teleported on Alice's qubit (q0)
qc.x(0)  # Applying a NOT gate to make it |1⟩ state
qc.h(0)  # Applying a Hadamard gate

# Perform Bell measurement on Alice's qubit (q0) and her half of the Bell pair (q1)
qc.cx(0, 1)
qc.h(0)

# Measure Alice's qubit (q0) and store the result in the classical register (c0)
qc.measure(0, 0)

# Apply gates to Bob's qubit (q2) based on measurement outcomes
qc.z(2).c_if(0, 1)  # Apply Z gate if the outcome of Alice's measurement was '1'
qc.x(2).c_if(0, 1)  # Apply X gate if the outcome of Alice's measurement was '1'

# Simulate the circuit on a classical computer
simulator = Aer.get_backend('qasm_simulator')
compiled_circuit = transpile(qc, simulator)
job = execute(compiled_circuit, simulator, shots=1000)
result = job.result()

# Get the measurement outcomes
counts = result.get_counts(qc)

# Analyze the measurement outcomes
print("Measurement outcomes:", counts)
