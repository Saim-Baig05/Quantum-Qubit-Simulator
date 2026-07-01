import random
import math
def Pauli_gate(amplitude_one):

    probability_of_zero = 1.0 - (amplitude_one ** 2)
    new_amplitude_one = math.sqrt(probability_of_zero)

    return new_amplitude_one

def stimulate_quantum_qubit(new_amplitude_one):
    probability_of_one = new_amplitude_one ** 2

    measurement = random.random()

    if measurement < probability_of_one:
        return 1
    else:
        return 0 

print("--- Quantum Gate Simulator (Pauli_X) ---")   

# chance of being 80% for 1 
starting_amplitude = math.sqrt(0.80)
print(f"Starting setup: 80% chance of landing on 1")

#Now swapping 80% to 0
flipped_amplitude = Pauli_gate(starting_amplitude)
print("Applied Pauli-X-Gate! The Percentage has been swapped.")

#Displaying result
result = stimulate_quantum_qubit(flipped_amplitude)
print(f"Result : Qubit Collapsed to {result}")


