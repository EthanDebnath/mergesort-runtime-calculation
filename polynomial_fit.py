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


# Fit a polynomial of degree 2 (quadratic) to the time data
poly_fit = np.polyfit(n_values, times, 2)

# Generate polynomial curve for plotting
poly_curve = np.polyval(poly_fit, n_values)

# Plot the actual timing data along with the polynomial fit
plt.plot(n_values, times, label='Actual Time', marker='o')
plt.plot(n_values, poly_curve, label=f'Fitted Polynomial (degree 2)', linestyle='--')
plt.xlabel('n (Input Size)')
plt.ylabel('Time (seconds)')
plt.title('Time vs n with Polynomial Fit')
plt.legend()
plt.grid(True)
plt.show()
