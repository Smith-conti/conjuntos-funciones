import matplotlib
matplotlib.use('Agg')

from flask import Flask, render_template, request
from matplotlib import pyplot as plt
from matplotlib_venn import venn2
import numpy as np
import os

app = Flask(__name__)

# ================================================
#   DEFINICIÓN DE CONJUNTOS A Y B
# ================================================
A = set([1,2,3,4,-4,-5,-6,23,25,27,100,200,240,240])
B = set([-4,-5,-6,300,400,600,500,500])

# ================================================
#   FUNCIONES OPERACIONES ENTRE CONJUNTOS
# ================================================
def cardinalA(): return len(A)
def cardinalB(): return len(B)
def union(): return A | B
def diferenciaA(): return A - B
def diferenciaB(): return B - A
def interseccion(): return A & B

# ================================================
#   FUNCIONES DIAGRAMAS VENN
# ================================================
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

# ================================================
#   RUTAS DEL SISTEMA
# ================================================
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

@app.route("/caso2/f1")
def caso2_menu():
    return render_template("caso2_f1.html")


@app.route("/caso2/f1", methods=["GET", "POST"])
def caso2_f1():
    resultado = None
    f1 = lambda x: x**2 + 3
    
    if request.method == "POST":
        x = float(request.form["x"])
        resultado = f"f(x) = {f1(x)}"
    
    return render_template("caso2_f1.html", resultado=resultado)


@app.route("/caso2/f2", methods=["GET", "POST"])
def caso2_f2():
    resultado = None
    f2 = lambda x, y: x**2 + y**2
    
    if request.method == "POST":
        x = float(request.form["x"])
        y = float(request.form["y"])
        resultado = f"f(x,y) = {f2(x, y)}"
    
    return render_template("caso2_f2.html", resultado=resultado)


@app.route("/caso2/compuesta", methods=["GET", "POST"])
def caso2_comp():
    resultado = None
    x_val = None
    g_val = None
    f_val = None

    f = lambda x: 2*x + 1       # f(x) = 2x + 1
    g = lambda x: x**2          # g(x) = x²

    if request.method == "POST":
        x_val = float(request.form["x"])
        g_val = g(x_val)
        f_val = f(g_val)
        resultado = f_val

    return render_template(
        "caso2_comp.html",
        resultado=resultado,
        x=x_val,
        g=g_val,
        f=f_val
    )


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
