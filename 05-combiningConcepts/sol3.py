# Implement a Qiskit program that prepares a qubit in an arbitrary superposition state and measures it to verify the expected probabilities.

from qiskit import QuantumCircuit, Aer, transpile, execute
from qiskit.visualization import plot_histogram

# Define the probabilities for the superposition state
p_0 = 0.3  # Probability of |0⟩
p_1 = 1 - p_0  # Probability of |1⟩

# Create a quantum circuit with 1 qubit and 1 classical bit
qc = QuantumCircuit(1, 1)

# Apply a rotation gate to create the superposition state
from qiskit.extensions import Initialize
initial_state = [p_0**0.5, p_1**0.5]  # Amplitudes for |0⟩ and |1⟩
initialize_gate = Initialize(initial_state)
qc.append(initialize_gate, [0])

# Measure the qubit and map the result to the classical bit
qc.measure(0, 0)

# Simulate the circuit on a classical computer
simulator = Aer.get_backend('qasm_simulator')
compiled_circuit = transpile(qc, simulator)
job = execute(compiled_circuit, simulator, shots=1000)
result = job.result()

# Get the measurement outcomes
counts = result.get_counts(qc)

# Analyze the measurement outcomes and calculate expected probabilities
expected_prob_0 = p_0**2
expected_prob_1 = p_1**2

# Print the measurement outcomes and expected probabilities
print("Measurement outcomes:", counts)
print("Expected probabilities:")
print("|0⟩ Probability:", expected_prob_0)
print("|1⟩ Probability:", expected_prob_1)

# Visualize the measurement outcomes
plot_histogram(counts)
