import tkinter as tk
from tkinter import ttk, simpledialog, messagebox, scrolledtext
import numpy as np
import math

class CalculadoraAlgebraLineal:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Álgebra Lineal")
        self.root.geometry("900x700")

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill="both")

        self.setup_matrices_tab()
        self.setup_sistemas_tab()
        self.setup_vectores_tab()

    # -------------------------------------------
    def setup_matrices_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Matrices")

        self.output_matriz = scrolledtext.ScrolledText(frame, width=100, height=30)
        self.output_matriz.pack()

        btn = ttk.Button(frame, text="Iniciar operaciones con matrices", command=self.operaciones_matrices)
        btn.pack(pady=10)

    def operaciones_matrices(self):
        try:
            filas = int(simpledialog.askstring("Filas", "Ingrese número de filas:"))
            columnas = int(simpledialog.askstring("Columnas", "Ingrese número de columnas:"))
        except:
            messagebox.showerror("Error", "El tamaño de las matrices debe ser un número entero")
            return

        matriz_a = np.zeros((filas, columnas))
        matriz_b = np.zeros((filas, columnas))
        for i in range(filas):
            for j in range(columnas):
                matriz_a[i][j] = float(simpledialog.askstring("Matriz A", f"A[{i+1},{j+1}] = "))
                matriz_b[i][j] = float(simpledialog.askstring("Matriz B", f"B[{i+1},{j+1}] = "))

        texto = f"Matriz A:\n{matriz_a}\n\nMatriz B:\n{matriz_b}\n\n"

        if matriz_a.shape == matriz_b.shape:
            suma = matriz_a + matriz_b
            texto += f"Suma A + B:\n{suma}\n\n"
        else:
            texto += "Las matrices no se pueden sumar (tamaños diferentes).\n\n"

        try:
            multiplicacion = np.dot(matriz_a, matriz_b)
            texto += f"Multiplicación A x B:\n{multiplicacion}\n"
        except:
            texto += "Las matrices no se pueden multiplicar (tamaños no coherentes).\n"

        self.output_matriz.delete("1.0", tk.END)
        self.output_matriz.insert(tk.END, texto)

    # -------------------------------------------
    def setup_sistemas_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Sistemas de Ecuaciones")

        self.output_sistemas = scrolledtext.ScrolledText(frame, width=100, height=30)
        self.output_sistemas.pack()

        btn = ttk.Button(frame, text="Resolver sistema", command=self.resolver_sistema)
        btn.pack(pady=10)

    def resolver_sistema(self):
        n = int(simpledialog.askstring("Tamaño", "Ingrese el tamaño del sistema (2 para 2x2, 3 para 3x3):"))
        A = np.zeros((n, n))
        B = np.zeros((n, 1))
        for i in range(n):
            for j in range(n):
                A[i][j] = float(simpledialog.askstring("Matriz A", f"A[{i+1},{j+1}] = "))
            B[i][0] = float(simpledialog.askstring("Vector B", f"B[{i+1}] = "))

        texto = f"Matriz A:\n{A}\n\nVector B:\n{B}\n\n"
        det_a = np.linalg.det(A)
        texto += f"Determinante |A| = {det_a:.2f}\n"

        if det_a == 0:
            texto += "El sistema no tiene solución |A| = 0 y la matriz A no tiene inversa.\n"
        else:
            # Método de Cramer
            soluciones_cramer = []
            for i in range(n):
                Ai = np.copy(A)
                Ai[:, i] = B[:, 0]
                det_ai = np.linalg.det(Ai)
                soluciones_cramer.append(det_ai / det_a)
                texto += f"Matriz A{i+1} (con columna {i+1} reemplazada):\n{Ai}\n"
                texto += f"Determinante |A{i+1}| = {det_ai:.2f}\n"
            texto += f"Solución con Cramer: {soluciones_cramer}\n\n"

            # Método de matriz inversa
            A_inv = np.linalg.inv(A)
            X = np.dot(A_inv, B)
            texto += f"Inversa de A:\n{A_inv}\n"
            texto += f"Solución con matriz inversa: {X.flatten()}\n"

        self.output_sistemas.delete("1.0", tk.END)
        self.output_sistemas.insert(tk.END, texto)

    # -------------------------------------------
    def setup_vectores_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Vectores")

        self.output_vectores = scrolledtext.ScrolledText(frame, width=100, height=30)
        self.output_vectores.pack()

        btn = ttk.Button(frame, text="Operar vectores", command=self.operar_vectores)
        btn.pack(pady=10)

    def operar_vectores(self):
        mag1 = float(simpledialog.askstring("Vector A", "Magnitud del vector A:"))
        ang1_deg = float(simpledialog.askstring("Vector A", "Ángulo (°) del vector A:"))
        mag2 = float(simpledialog.askstring("Vector B", "Magnitud del vector B:"))
        ang2_deg = float(simpledialog.askstring("Vector B", "Ángulo (°) del vector B:"))

        ang1_rad = math.radians(ang1_deg)
        ang2_rad = math.radians(ang2_deg)

        Ax, Ay = mag1 * math.cos(ang1_rad), mag1 * math.sin(ang1_rad)
        Bx, By = mag2 * math.cos(ang2_rad), mag2 * math.sin(ang2_rad)

        texto = f"Vector A: ({Ax:.2f}, {Ay:.2f})\nVector B: ({Bx:.2f}, {By:.2f})\n\n"

        # Suma
        Cx, Cy = Ax + Bx, Ay + By
        mag_C = math.sqrt(Cx**2 + Cy**2)
        ang_C = math.degrees(math.atan2(Cy, Cx))
        texto += f"Suma: ({Cx:.2f}, {Cy:.2f})\nMagnitud: {mag_C:.2f}, Ángulo: {ang_C:.2f}°\n\n"

        # Producto punto
        dot = Ax * Bx + Ay * By
        texto += f"Producto punto: {dot:.2f}\n"

        # Ángulo entre vectores
        cos_theta = dot / (mag1 * mag2)
        angle_between = math.degrees(math.acos(cos_theta))
        texto += f"Ángulo entre vectores: {angle_between:.2f}°\n\n"

        # Producto cruz (2D se considera solo la componente z)
        cross = Ax * By - Ay * Bx
        texto += f"Producto cruz (componente Z): {cross:.2f}\n"

        self.output_vectores.delete("1.0", tk.END)
        self.output_vectores.insert(tk.END, texto)

# Ejecutar aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraAlgebraLineal(root)
    root.mainloop()
