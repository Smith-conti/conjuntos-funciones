# Función para quitar .0 innecesarios
def fnum(n):
    return int(n) if float(n).is_integer() else n

# f(x,y) = x² + y²
def f(x, y):
    return x**2 + y**2

print("=== Ejemplos ===\n")
print("f(2,3) =", f(2,3))
print("f(5,-3) =", f(5,-3))

print("\n=== Evaluación de f(x,y) = x² + y² ===")
x = float(input("Ingrese valor para x: "))
y = float(input("Ingrese valor para y: "))

x_f, y_f = fnum(x), fnum(y)
t1 = fnum(x**2)
t2 = fnum(y**2)
total = fnum(f(x,y))

print("\nResultado:")
print(f"f({x_f}, {y_f}) = {total}")

print("\nPasos:")
print(f"Sustitución: f({x_f}, {y_f}) = ({x_f})² + ({y_f})²")
print(f"Cálculo: {x_f}² = {t1}, {y_f}² = {t2}")
print(f"Sumando: {t1} + {t2} = {total}")
