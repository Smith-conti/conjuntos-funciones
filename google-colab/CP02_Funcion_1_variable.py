# Función para quitar .0 innecesarios
def fnum(n):
    return int(n) if float(n).is_integer() else n

# f(x) = x² + 3
def f1(x):
    return x**2 + 3

print("=== Ejemplos ===\n")
print("f(-5) =", f(-5))
print("f(-1) =", f(-1))
print("f(4) + f(3) =", f(4) + f(3))

print("\n=== Evaluación de f(x) = x² + 3 ===")
x = float(input("\nIngrese un valor para x: "))

x_f = fnum(x)
t1 = fnum(x**2)
total = fnum(f1(x))

print("\nResultado:")
print(f"f({x_f}) = {total}")

print("\nPasos:")
print(f"Sustitución: f({x_f}) = ({x_f})² + 3")
print(f"Cálculo: {x_f}² = {t1}")
print(f"Sumando: {t1} + 3 = {total}")
