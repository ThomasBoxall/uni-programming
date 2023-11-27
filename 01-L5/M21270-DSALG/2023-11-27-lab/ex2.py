import matplotlib.pyplot as plt
# Modulo Hashing Function
def modulo_hashing(keys, m):
    hash_table = [0] * m
    for key in keys:
        hash_table[key % m] += 1
    return hash_table
# Modulo Hashing Analysis Function
def modulo_hashing_analysis(keys, m_values):
    analysis_results = {}
    for m in m_values:
        hash_table = [0] * m
        for key in keys:
            hash_table[key % m] += 1
        # Count collisions (slots with more than one key)
        collisions = sum(1 for slot in hash_table if slot > 1)
        analysis_results[m] = (collisions, m)
    return analysis_results
# Original keys
keys = [5, 10, 12, 14, 17, 25, 27, 30, 33, 45, 56, 64, 128, 129]
# Original hash table size
m_original = 7
# Apply hashing with original m
original_distribution = modulo_hashing(keys, m_original)
# Analyzing collisions for a range of m values
m_values = range(5, 50) # Trying values from 5 to 49
collision_analysis = modulo_hashing_analysis(keys, m_values)
# Finding the m with the minimum collisions
min_collisions_m = min(collision_analysis, key=lambda m:
collision_analysis[m][0])
min_collisions, optimal_m = collision_analysis[min_collisions_m]
# Plotting
fig, axes = plt.subplots(2, 1, figsize=(12, 12))
# Plot 1: Original Distribution
axes[0].bar(range(m_original), original_distribution)
axes[0].set_title(f'Original Hash Table Distribution (m={m_original})')
axes[0].set_xlabel('Hash Value')
axes[0].set_ylabel('Number of Keys')
# Plot 2: Collision Analysis
m_values_plot = list(collision_analysis.keys())
collisions_plot = [collision_analysis[m][0] for m in m_values_plot]
axes[1].plot(m_values_plot, collisions_plot, label='Number of Collisions', color='red', marker='o')
axes[1].axvline(x=min_collisions_m, color='green', linestyle='--',
label=f'Optimal m = {min_collisions_m}')
axes[1].set_title('Collision Analysis for Different Hash Table Sizes')
axes[1].set_xlabel('Hash Table Size (m)')
axes[1].set_ylabel('Number of Collisions')
axes[1].legend()
axes[1].grid(True)
# Show the plot
plt.tight_layout()
plt.show()
min_collisions_m, min_collisions, optimal_m