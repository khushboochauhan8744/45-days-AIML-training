import numpy as np
import matplotlib.pyplot as plt

# Generate random data arrays
uniform_samples = np.random.uniform(0, 10, 1000)
normal_samples = np.random.normal(5, 2, 1000)

# Calculate and print basic stats
print("--- Uniform Distribution Stats ---")
print("Mean:", np.mean(uniform_samples))
print("Standard Deviation:", np.std(uniform_samples))

print("\n--- Normal Distribution Stats ---")
print("Mean:", np.mean(normal_samples))
print("Standard Deviation:", np.std(normal_samples))

# Create side-by-side plots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

# Left chart: Uniform
ax1.hist(uniform_samples, bins=15, color="skyblue", edgecolor="black")
ax1.set_title("Uniform (Flat Shape)")

# Right chart: Normal
ax2.hist(normal_samples, bins=15, color="salmon", edgecolor="black")
ax2.set_title("Normal (Bell Shape)")

plt.show()