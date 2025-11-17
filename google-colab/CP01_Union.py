!pip install matplotlib-venn

from matplotlib import pyplot as plt
from matplotlib_venn import venn2

A = set([1,2,3,4,-4,-5,-6,23,25,27,100,200,240])
B = set([-4,-5,-6,300,400,600,500])

U = A | B
print("A ∪ B =", U)

plt.figure(figsize=(6,6))
v = venn2([A, B], set_labels=('A', 'B'))

for area in ("10","01","11"):
    if v.get_patch_by_id(area):
        v.get_patch_by_id(area).set_color("skyblue")

plt.title("Unión A ∪ B")
plt.show(block=False)
plt.pause(0.1)
