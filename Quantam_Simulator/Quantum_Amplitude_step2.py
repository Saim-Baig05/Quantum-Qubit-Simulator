import math
import random
def stimulate_quantam_qubit(amplitude_one):
    print("---Quantam Qubit Simulator---")
    probability_of_one = amplitude_one ** 2
    print(f"Given Amplitude for 1 :{amplitude_one}")
    print(f"Calculated Probability : {probability_of_one*100} % chance of being 1")
    measurement = random.random()
    if measurement < probability_of_one:
        return 1
    else:
        return 0

Target_Amplitude =math.sqrt(0.5)
result = stimulate_quantam_qubit(Target_Amplitude)
print(f"Result of Measurement : Qubit Collapsed to {result}")
