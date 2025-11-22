# Función para quitar .0 innecesarios
def fnum(n):
    return int(n) if float(n).is_integer() else n

# g(x) = x²
def g(x):
    return x**2

# f(u) = 2u + 1
def f(u):
    return 2*u + 1

print("=== Ejemplos ===\n")
print("f(g(-5)) =", f(g(-5)))
print("f(g(-2)) =", f(g(-2)))

print("\n=== Evaluación de f(g(x)) ===")
x = float(input("Ingrese valor para x: "))

x_f = fnum(x)

g_val = fnum(g(x))
f_val = fnum(f(g_val))

print("\nResultado:")
print(f"f(g({x_f})) = {f_val}")

print("\nPasos:")
print(f"Calcular g({x_f}) = ({x_f})² = {g_val}")
print(f"Sustituir en f(g) = 2g+1 → f({g_val}) = 2({g_val}) + 1")
print(f"Resultado final: 2({g_val}) + 1 = {f_val}")
