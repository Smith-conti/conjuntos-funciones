import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 200)
y = x**2 + 2

plt.plot(x, y)
plt.grid(True)
plt.xlabel("x")
plt.ylabel("f(x) = x² + 2")
plt.title("Gráfica de f(x) = x² + 2")
plt.show()
