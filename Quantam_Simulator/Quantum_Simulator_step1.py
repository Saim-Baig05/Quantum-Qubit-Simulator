import random
def stimulate_qubit(probability_of_one):
    print("---Quantam Qubit Simulator---")
    print(f"setting Qubit state:{probability_of_one * 100}% chance of being one ")

    measurement = random.random()
    if measurement > probability_of_one:
        return 0
    else:
        return 1

result = stimulate_qubit(0.7)
print(f"Result of Meauserment : Qubit Collapsed to {result}")
