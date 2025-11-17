!pip install matplotlib-venn

from matplotlib import pyplot as plt
from matplotlib_venn import venn2

A = set([1,2,3,4,-4,-5,-6,23,25,27,100,200,240])
B = set([-4,-5,-6,300,400,600,500])

D = A - B
print("A - B =", D)

plt.figure(figsize=(6,6))
v = venn2([A, B], set_labels=('A', 'B'))

if v.get_patch_by_id("10"):
    v.get_patch_by_id("10").set_color("lightgreen")
if v.get_patch_by_id("11"):
    v.get_patch_by_id("11").set_color("white")

plt.title("Diferencia A - B")
plt.show(block=False)
plt.pause(0.1)
