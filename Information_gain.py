import numpy as np

def entropy(p):
    if p == 0 or p == 1:
        return 0
    return -np.sum([p * np.log2(p) + (1 - p) * np.log2(1 - p)])

def input_fraction(prompt="Enter a fraction (e.g., 3/4): "):
    fraction_str = input(prompt)
    if '/' not in fraction_str:
        return float(fraction_str)
    numerator, denominator = map(float, fraction_str.split('/'))
    return numerator / denominator

print("Before split value:")
y = input_fraction()
print("Entropy of the before-split values is: ", entropy(y))

a = input("Enter the number of features:")
information_gains = []

for i in range(int(a)):
    print("Feature", i + 1)
    print("True")
    x = input_fraction()
    print("Entropy given True: ", entropy(x))
    print("False")
    z = input_fraction()
    print("Entropy given False: ", entropy(z))
    print("Enter the true probability: ")
    t = input_fraction()
    entropy_after_split = t * entropy(x) + (1 - t) * entropy(z)
    print("Entropy after split: ", entropy_after_split)
    ig= entropy(y) - entropy_after_split
    print(ig)
    information_gains.append(ig)
    print("Information gain of feature", i + 1, "is:", ig)
    print(" ")

max_information_gain = max(information_gains)
max_feature_index = information_gains.index(max_information_gain) + 1
print("The feature with the maximum information gain is feature", max_feature_index, "with information gain", max_information_gain)