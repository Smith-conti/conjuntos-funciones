def f(x): return 2*x + 1
def g(x): return x**2

print("f(g(-5)) =", f(g(-5)))
print("f(g(-2)) =", f(g(-2)))

x = float(input("Ingrese x: "))
print("f(g(x)) =", f(g(x)))
