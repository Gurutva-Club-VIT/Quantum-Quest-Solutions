# Write a Qiskit program that prepares the Bell state |Φ-⟩ = (|00⟩ - |11⟩) / √2 using Hadamard and CNOT gates. Measure both qubits and discuss outcomes.

from qiskit import QuantumCircuit, Aer, transpile, execute
from qiskit.visualization import plot_histogram

# Create a quantum circuit with 2 qubits
qc = QuantumCircuit(2, 2)

# Apply a Hadamard gate to the first qubit
qc.h(0)

# Apply an X gate to the second qubit
qc.x(1)

# Apply a CNOT gate from the first qubit (control) to the second qubit (target)
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

# Discuss the outcomes
print("Measurement outcomes:", counts)

# Theoretically, you should see '00' and '11' with equal probabilities.
