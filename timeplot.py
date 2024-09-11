import time
import matplotlib.pyplot as plt
import numpy as np

# Define the original function
def f(n):
    x = 1
    for i in range(1, n+1):
        for j in range(1, n+1):
            x += 1

# Test for various n values
n_values = list(range(1, 1001, 10))  # Vary n from 1 to 1000 with step of 10
times = []

# Measure time taken for each n
for n in n_values:
    start_time = time.time()
    f(n)
    end_time = time.time()
    times.append(end_time - start_time)

# Plot time vs n
plt.plot(n_values, times, label="Actual Time")
plt.xlabel('n (Input Size)')
plt.ylabel('Time (seconds)')
plt.title('Time vs n')
plt.legend()
plt.grid(True)
plt.show()
