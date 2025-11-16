# 📘 Teoría de Conjuntos, Relaciones y Funciones

### Aplicación Web en Python con Flask + Bootstrap

Este proyecto implementa casos prácticos de teoría de conjuntos y
funciones utilizando una interfaz web moderna con **Flask**,
**Bootstrap**, **Matplotlib** y **matplotlib-venn**.

Permite ejecutar:

-   **Caso 1:** Operaciones entre conjuntos (con generación automática
    de diagramas de Venn).\
-   **Caso 2:** Evaluación de funciones individualmente y generación
    dinámica de gráficas.

------------------------------------------------------------------------

## 📌 Requisitos del sistema

-   ✔ Python **3.10 -- 3.12**\
-   ✔ Pip actualizado\
-   ✔ Git (opcional pero recomendado)

------------------------------------------------------------------------

## 📥 1. Clonar el repositorio

``` bash
git clone https://github.com/usuario/tu-repositorio.git
cd tu-repositorio
```

------------------------------------------------------------------------

## 🧰 2. Crear entorno virtual

### 🪟 Windows

``` bash
python -m venv venv
venv\Scripts\activate
```

### 🐧 Linux / macOS

``` bash
python3 -m venv venv
source venv/bin/activate
```

------------------------------------------------------------------------

## 📦 3. Instalar dependencias

### Windows

``` bash
pip install -r requirements.txt
```

### Linux / macOS

``` bash
pip3 install -r requirements.txt
```

------------------------------------------------------------------------

## 📚 4. Archivo `requirements.txt` recomendado

    Flask
    matplotlib
    matplotlib-venn
    numpy

------------------------------------------------------------------------

## ▶️ 5. Ejecutar la aplicación localmente

Con el entorno virtual activo:

### Windows

``` bash
python app.py
```

### Linux / macOS

``` bash
python3 app.py
```

El servidor iniciará en:

👉 **http://127.0.0.1:5000/**

------------------------------------------------------------------------

## 🖼 6. Archivos generados

Las imágenes generadas (diagramas de Venn y gráficas) se guardan
automáticamente en:

    static/

------------------------------------------------------------------------

## 🛑 Desactivar el entorno virtual

``` bash
deactivate
```

------------------------------------------------------------------------

## 🧩 Estructura del proyecto

    proyecto_conjuntos/
    │── app.py
    │── requirements.txt
    │── static/
    │     ├── venn.png
    │     └── funcion.png
    │── templates/
    │     ├── index.html
    │     ├── caso1.html
    │     ├── caso2_menu.html
    │     ├── caso2_f1.html
    │     ├── caso2_f2.html
    │     ├── caso2_comp.html
    │     └── caso2_graf.html
    └── README.md

------------------------------------------------------------------------

## ⚙️ Notas importantes

### 🔹 Problemas con Tkinter

Este proyecto usa Matplotlib con backend no interactivo.\
Asegúrate de incluir al inicio de `app.py`:

``` python
import matplotlib
matplotlib.use('Agg')
```

### 🔹 Si pip3 no está instalado (Linux)

``` bash
sudo apt install python3-pip
```

### 🔹 Instalar virtualenv si es necesario

``` bash
pip install virtualenv
```
