import math

def entropy(examples):
    total = len(examples)
    if total == 0: return 0.0
    pos = sum(1 for row in examples if row[-1] == 'Yes')
    neg = total - pos
    if pos == 0 or neg == 0: return 0.0
    p_pos = pos / total
    p_neg = neg / total
    return -(p_pos * math.log2(p_pos) + p_neg * math.log2(p_neg))

def info_gain(examples, attr_idx):
    total_entropy = entropy(examples)
    vals = set(row[attr_idx] for row in examples)
    weighted_entropy = 0.0
    for v in vals:
        subset = [row for row in examples if row[attr_idx] == v]
        weighted_entropy += (len(subset) / len(examples)) * entropy(subset)
    return total_entropy - weighted_entropy

# Standard PlayTennis Dataset: [Outlook, Temp, Humidity, Wind, PlayTennis]
attributes = ['Outlook', 'Temperature', 'Humidity', 'Wind']
dataset = [
    ['Sunny', 'Hot', 'High', 'Weak', 'No'],
    ['Sunny', 'Hot', 'High', 'Strong', 'No'],
    ['Overcast', 'Hot', 'High', 'Weak', 'Yes'],
    ['Rain', 'Mild', 'High', 'Weak', 'Yes'],
    ['Rain', 'Cool', 'Normal', 'Weak', 'Yes'],
    ['Rain', 'Cool', 'Normal', 'Strong', 'No'],
    ['Overcast', 'Cool', 'Normal', 'Strong', 'Yes'],
    ['Sunny', 'Mild', 'High', 'Weak', 'No'],
    ['Sunny', 'Cool', 'Normal', 'Weak', 'Yes'],
    ['Rain', 'Mild', 'Normal', 'Weak', 'Yes'],
    ['Sunny', 'Mild', 'Normal', 'Strong', 'Yes'],
    ['Overcast', 'Mild', 'High', 'Strong', 'Yes'],
    ['Overcast', 'Hot', 'Normal', 'Weak', 'Yes'],
    ['Rain', 'Mild', 'High', 'Strong', 'No']
]

print("Decision Tree (ID3 Algorithm) Classification:\n")
print(f"Total Training Instances: {len(dataset)}")
print(f"Attributes: {attributes}")
print(f"Base Entropy of Dataset: {entropy(dataset):.4f}\n")

print("Information Gain for Attributes:")
best_gain, root_attr = -1, None
for i, attr in enumerate(attributes):
    gain = info_gain(dataset, i)
    print(f"  Gain(S, {attr:11}) = {gain:.4f}")
    if gain > best_gain:
        best_gain, root_attr = gain, attr

print(f"\nSelected Root Decision Node: {root_attr} (Max Gain: {best_gain:.4f})")