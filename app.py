import matplotlib
from flask import Flask, render_template, request, redirect, flash
from matplotlib import pyplot as plt
from matplotlib_venn import venn2
import numpy as np
import os
from flask import flash

matplotlib.use('Agg')
app = Flask(__name__)
app.secret_key = "JGF73hs8_2hshsA82hs72HahH27as!92"

# Formatear numeros 0.0 = 0
def fnum(n):
    return int(n) if float(n).is_integer() else n

# ================================================
#   CASO 1
# ================================================

#   DEFINICIÓN DE CONJUNTOS A Y B

A = set([1,2,3,4,-4,-5,-6,23,25,27,100,200,240,240])
B = set([-4,-5,-6,300,400,600,500,500])

#   FUNCIONES OPERACIONES ENTRE CONJUNTOS

def cardinalA(): return len(A)
def cardinalB(): return len(B)
def union(): return A | B
def diferenciaA(): return A - B
def diferenciaB(): return B - A
def interseccion(): return A & B

#   FUNCIONES DIAGRAMAS VENN

def generar_venn(op, titulo):
    plt.figure(figsize=(6,6))
    v = venn2([A, B], set_labels=('A', 'B'))

    if op == "union":
        for sub in ("10","01","11"):
            if v.get_patch_by_id(sub):
                v.get_patch_by_id(sub).set_color("skyblue")

    elif op == "diferenciaA":
        if v.get_patch_by_id("10"):
            v.get_patch_by_id("10").set_color("lightgreen")

    elif op == "diferenciaB":
        if v.get_patch_by_id("01"):
            v.get_patch_by_id("01").set_color("orange")

    elif op == "interseccion":
        if v.get_patch_by_id("11"):
            v.get_patch_by_id("11").set_color("yellow")

    plt.title(titulo)

    # Guardar imagen en la carpeta static
    img_path = os.path.join("static", "venn.png")
    plt.savefig(img_path)
    plt.close()

#   RUTAS DEL SISTEMA

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/caso1", methods=["GET", "POST"])
def caso1():
    resultado = ""
    venn_image = None

    if request.method == "POST":
        opcion = request.form["opcion"]

        if opcion == "cardA":
            resultado = f"Cardinal de A = {cardinalA()}"
            generar_venn("union", "Conjuntos A y B")
        elif opcion == "cardB":
            resultado = f"Cardinal de B = {cardinalB()}"
            generar_venn("union", "Conjuntos A y B")
        elif opcion == "union":
            resultado = f"Unión A ∪ B = {union()}"
            generar_venn("union", "Unión A ∪ B")
        elif opcion == "difA":
            resultado = f"Diferencia A - B = {diferenciaA()}"
            generar_venn("diferenciaA", "Diferencia A - B")
        elif opcion == "difB":
            resultado = f"Diferencia B - A = {diferenciaB()}"
            generar_venn("diferenciaB", "Diferencia B - A")
        elif opcion == "inter":
            resultado = f"Intersección A ∩ B = {interseccion()}"
            generar_venn("interseccion", "Intersección A ∩ B")

        venn_image = "venn.png"

    return render_template("caso1.html", resultado=resultado, venn_image=venn_image)


# ================================================
#   CASO 2
# ================================================

# Función de una sola variable
@app.route("/caso2/f1", methods=["GET", "POST"])
def caso2_f1():
    resultado = None
    pasos = []
    
    f1 = lambda x: x**2 + 3

    if request.method == "POST":

        # Validación de campos vacios
        if request.form["x"].strip() == "":
            flash("⚠ Por favor inserte valores para X", "danger")
            return redirect("/caso2/f1")

        x = float(request.form["x"])

        x_f = fnum(x)
        term1 = fnum(x**2)
        term2 = 3
        total = fnum(f1(x))

        pasos = [
            f"f({x_f}) = ({x_f})² + 3",
            f"{x_f}² = {term1}",
            f"{term1} + 3 = {total}"
        ]

        resultado = f"f({x_f}) = {total}"

    return render_template("caso2_f1.html", resultado=resultado, pasos=pasos)


# Función de dos variables
@app.route("/caso2/f2", methods=["GET", "POST"])
def caso2_f2():
    resultado = None
    pasos = []

    f2 = lambda x, y: x**2 + y**2

    if request.method == "POST":

        # Validación de campos vacios
        if request.form["x"].strip() == "" or request.form["y"].strip() == "":
            flash("⚠ Por favor inserte valores para X Y", "danger")
            return redirect("/caso2/f2")

        x = float(request.form["x"])
        y = float(request.form["y"])

        x_f, y_f = fnum(x), fnum(y)
        term1 = fnum(x**2)
        term2 = fnum(y**2)
        total = fnum(f2(x,y))

        pasos = [
            f"f({x_f}, {y_f}) = ({x_f})² + ({y_f})²",
            f"{x_f}² = {term1}",
            f"{y_f}² = {term2}",
            f"{term1} + {term2} = {total}"
        ]

        resultado = f"f({x_f}, {y_f}) = {total}"

    return render_template("caso2_f2.html", resultado=resultado, pasos=pasos)


# Función compuesta
@app.route("/caso2/compuesta", methods=["GET", "POST"])
def caso2_comp():
    resultado = None
    pasos = []

    g = lambda x: x**2
    f = lambda u: 2*u + 1

    if request.method == "POST":

        # Validación de campos vacios
        if request.form["x"].strip() == "":
            flash("⚠ Por favor inserte valores para X.", "danger")
            return redirect("/caso2/compuesta")

        x = float(request.form["x"])

        x_f = fnum(x)
        g_val = fnum(g(x))
        f_val = fnum(f(g_val))

        pasos = [
            f"f(g(x)) = 2(x²) + 1 ===> f(g({x_f})) = 2(({x_f})²) +1",
            f"• g({x_f}) = ({x_f})² = {g_val}",
            f"• f({g_val}) = 2({g_val}) + 1",
            f"2({g_val}) + 1 = {f_val}"
        ]

        resultado = f"f(g({x_f})) = {f_val}"

    return render_template("caso2_comp.html", resultado=resultado, pasos=pasos)


# Gráfica de funciones
@app.route("/caso2/grafica", methods=["GET", "POST"])
def caso2_graf():
    grafica = None
    
    if request.method == "POST":
        x = np.linspace(-10, 10, 200)
        y = x**2 + 2

        plt.plot(x, y)
        plt.title("f(x) = x² + 2")
        plt.grid(True)
        plt.savefig("static/funcion.png")
        plt.close()

        grafica = "funcion.png"

    return render_template("caso2_graf.html", grafica=grafica)


if __name__ == "__main__":
    app.run(debug=True)
