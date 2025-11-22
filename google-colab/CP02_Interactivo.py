# Funciones paso a paso

!pip install ipywidgets sympy --quiet

from IPython.display import display, Markdown, clear_output
import ipywidgets as widgets
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# FUNCION PARA FORMATEAR NÚMEROS SIN ".0"
def fnum(n):
    return int(n) if float(n).is_integer() else n

# ======================================================
# FUNCIONES
# ======================================================

# f(x) = x^2 + 3
def f1(x):
    return x**2 + 3

# f(x,y) = x^2 + y^2
def f2(x, y):
    return x**2 + y**2

# g(x) = x^2
def g(x):
    return x**2

# f(u) = 2u + 1
def f_comp(u):
    return 2*u + 1


# ======================================================
# WIDGETS — f(x)
# ======================================================

title_fx = Markdown("## Función de una variable:  \n### $f(x) = x^2 + 3$")
input_fx = widgets.FloatText(description="x =")
button_fx = widgets.Button(description="Calcular paso a paso", button_style="primary")
out_fx = widgets.Output()

def calc_fx(b):
    with out_fx:
        clear_output()
        x = input_fx.value
        x_f = fnum(x)

        t1 = fnum(x**2)
        total = fnum(f1(x))

        display(Markdown(f"### Resultado:  \n**f({x_f}) = {total}**"))
        display(Markdown("### Pasos:"))
        display(Markdown(f"- Sustitución:  \n  $f({x_f}) = ({x_f})^2 + 3$"))
        display(Markdown(f"- Cálculo:  \n  ({x_f})² = {t1}"))
        display(Markdown(f"- Suma final:  \n  {t1} + 3 = {total}"))
        display(Markdown(f"\n\n### **Resultado: {total}**"))

button_fx.on_click(calc_fx)


# ======================================================
# WIDGETS — f(x,y)
# ======================================================

title_fxy = Markdown("## Función de dos variables:  \n### $f(x,y) = x^2 + y^2$")
input_fx2 = widgets.FloatText(description="x =")
input_fy2 = widgets.FloatText(description="y =")
button_fxy = widgets.Button(description="Calcular paso a paso", button_style="info")
out_fxy = widgets.Output()

def calc_fxy(b):
    with out_fxy:
        clear_output()

        x = input_fx2.value
        y = input_fy2.value

        x_f, y_f = fnum(x), fnum(y)

        t1 = fnum(x**2)
        t2 = fnum(y**2)
        total = fnum(f2(x,y))

        display(Markdown(f"### Resultado:  \n**f({x_f}, {y_f}) = {total}**"))
        display(Markdown("### Pasos:"))
        display(Markdown(f"- Sustitución:  \n  $f({x_f},{y_f}) = ({x_f})^2 + ({y_f})^2$"))
        display(Markdown(f"- Cálculo:  \n  ({x_f})² = {t1},  ({y_f})² = {t2}"))
        display(Markdown(f"- Suma final:  \n  {t1} + {t2} = {total}"))
        display(Markdown(f"\n\n### **Resultado: {total}**"))

button_fxy.on_click(calc_fxy)


# ======================================================
# WIDGETS — f(g(x))
# ======================================================

title_comp = Markdown("## Función compuesta:  \n### $g(x)=x^2$  \n### $f(g)=2g+1$  \n### Evaluar: $f(g(x))$")
input_comp = widgets.FloatText(description="x =")
button_comp = widgets.Button(description="Calcular paso a paso", button_style="success")
out_comp = widgets.Output()

def calc_comp(b):
    with out_comp:
        clear_output()

        x = input_comp.value
        x_f = fnum(x)

        g_val = fnum(g(x))
        f_val = fnum(f_comp(g_val))

        display(Markdown(f"### Resultado:  \n**f(g({x_f})) = {f_val}**"))
        display(Markdown("### Pasos:"))
        display(Markdown(f"- Paso 1:  \n  $g({x_f}) = ({x_f})^2 = {g_val}$"))
        display(Markdown(f"- Paso 2:  \n  Sustituir en f(g) = 2g + 1 → $f({g_val}) = 2({g_val}) + 1$"))
        display(Markdown(f"- Paso 3:  \n  $2({g_val}) + 1 = {f_val}$"))
        display(Markdown(f"\n\n### **Resultado: {f_val}**"))

button_comp.on_click(calc_comp)


# ======================================================
# WIDGET — GRÁFICA f(x) = x^2 + 2
# ======================================================

title_graf = Markdown("## Gráfica de la función:  \n### $f(x) = x^2 + 2$")
button_graf = widgets.Button(description="Mostrar gráfica", button_style="warning")
out_graf = widgets.Output()

def calc_graph(b):
    with out_graf:
        clear_output()

        x = np.linspace(-10, 10, 200)
        y = x**2 + 2

        plt.figure(figsize=(6,4))
        plt.plot(x, y)
        plt.grid(True)
        plt.xlabel("x")
        plt.title("f(x) = x² + 2")

        plt.axhline(0, color="black", linewidth=0.5)
        plt.axvline(0, color="black", linewidth=0.5)

        plt.show()

button_graf.on_click(calc_graph)


# ======================================================
# MOSTRAR TODO EN PANTALLA
# ======================================================

display(title_fx)
display(widgets.HBox([input_fx, button_fx]))
display(out_fx)

display(Markdown("---"))

display(title_fxy)
display(widgets.HBox([input_fx2, input_fy2, button_fxy]))
display(out_fxy)

display(Markdown("---"))

display(title_comp)
display(widgets.HBox([input_comp, button_comp]))
display(out_comp)

display(Markdown("---"))

display(title_graf)
display(button_graf)
display(out_graf)
