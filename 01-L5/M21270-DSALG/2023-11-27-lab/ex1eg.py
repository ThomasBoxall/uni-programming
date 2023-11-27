import random
import matplotlib.pyplot as plt
# Function to perform modulo hashing
def modulo_hashing(keys, m):
    hash_table = [0] * m
    for key in keys:
        hash_table[key % m] += 1
    return hash_table
# Generate 100 random and unique integer keys
keys = random.sample(range(1000), 100)
# Different values of m
m_values = [10, 20, 50, 100, 200]
# Store results for each m
results = {}
# Hashing and storing results
for m in m_values:
    results[m] = modulo_hashing(keys, m)
# Plotting the results
fig, axes = plt.subplots(len(m_values), 1, figsize=(10, 20))
fig.suptitle('Distribution of Hash Values for Different m')
for i, m in enumerate(m_values):
    axes[i].bar(range(m), results[m])
    axes[i].set_title(f'm = {m}')
    axes[i].set_xlabel('Hash Value')
    axes[i].set_ylabel('Number of Keys')
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()