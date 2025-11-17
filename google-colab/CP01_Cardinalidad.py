!pip install matplotlib-venn

from matplotlib import pyplot as plt
from matplotlib_venn import venn2

A = set([1,2,3,4,-4,-5,-6,23,25,27,100,200,240])
B = set([-4,-5,-6,300,400,600,500])

print("Conjunto A =", A)
print("Conjunto B =", B)

print("\nCardinalidad |A| =", len(A))
print("Cardinalidad |B| =", len(B))

# DIAGRAMA GENERAL
plt.figure(figsize=(6,6))
v = venn2([A, B], set_labels=('A', 'B'))

plt.title("Diagrama Venn–Euler de A y B")
plt.show(block=False)
plt.pause(0.1)
