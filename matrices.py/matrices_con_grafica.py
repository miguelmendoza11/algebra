import tkinter as tk
from tkinter import simpledialog, messagebox, scrolledtext
import numpy as np

class MatrizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Operaciones con Matrices")
        
        self.matriz_a = None
        self.matriz_b = None

        tk.Label(root, text="Operaciones con Matrices", font=("Helvetica", 16, "bold")).pack(pady=10)
        
        btn_frame = tk.Frame(root)
        btn_frame.pack()

        botones = [
            ("Crear Matriz A", self.crear_matriz_a),
            ("Crear Matriz B", self.crear_matriz_b),
            ("Suma", self.sumar),
            ("Multiplicación", self.multiplicar),
            ("Det. Sarrus (3x3)", self.det_sarrus),
            ("Det. Cofactores", self.det_cofactores),
            ("Inversa", self.inversa),
            ("Método de Cramer", self.metodo_cramer)
        ]

        for texto, comando in botones:
            tk.Button(btn_frame, text=texto, width=18, command=comando).pack(pady=2)
        
        self.resultado_area = scrolledtext.ScrolledText(root, width=70, height=20)
        self.resultado_area.pack(pady=10)

    def mostrar_matriz(self, matriz, nombre):
        self.resultado_area.insert(tk.END, f"\n{nombre} =\n")
        for fila in matriz:
            self.resultado_area.insert(tk.END, "  " + "  ".join(f"{x:.2f}" for x in fila) + "\n")

    def crear_matriz_a(self):
        self.matriz_a = self.crear_matriz("A")
        self.resultado_area.insert(tk.END, "\nMatriz A creada:")
        self.mostrar_matriz(self.matriz_a, "A")
    
    def crear_matriz_b(self):
        self.matriz_b = self.crear_matriz("B")
        self.resultado_area.insert(tk.END, "\nMatriz B creada:")
        self.mostrar_matriz(self.matriz_b, "B")

    def crear_matriz(self, nombre):
        filas = simpledialog.askinteger("Filas", f"Ingrese el número de filas para matriz {nombre}:")
        columnas = simpledialog.askinteger("Columnas", f"Ingrese el número de columnas para matriz {nombre}:")
        matriz = []
        for i in range(filas):
            fila = []
            for j in range(columnas):
                valor = simpledialog.askfloat("Valor", f"{nombre}[{i+1},{j+1}] = ")
                fila.append(valor)
            matriz.append(fila)
        return matriz

    def sumar(self):
        if self.matriz_a and self.matriz_b:
            try:
                resultado = np.add(self.matriz_a, self.matriz_b).tolist()
                self.resultado_area.insert(tk.END, "\n\nResultado de A + B:")
                self.mostrar_matriz(resultado, "A + B")
            except:
                messagebox.showerror("Error", "Las matrices deben tener las mismas dimensiones.")
        else:
            messagebox.showinfo("Falta información", "Primero crea las matrices A y B.")

    def multiplicar(self):
        if self.matriz_a and self.matriz_b:
            try:
                resultado = np.dot(self.matriz_a, self.matriz_b).tolist()
                self.resultado_area.insert(tk.END, "\n\nResultado de A x B:")
                self.mostrar_matriz(resultado, "A x B")
            except:
                messagebox.showerror("Error", "Dimensiones no compatibles para multiplicación.")
        else:
            messagebox.showinfo("Falta información", "Primero crea las matrices A y B.")

    def det_sarrus(self):
        if self.matriz_a and len(self.matriz_a) == 3 and len(self.matriz_a[0]) == 3:
            m = self.matriz_a
            det = (m[0][0]*m[1][1]*m[2][2] + m[0][1]*m[1][2]*m[2][0] + m[0][2]*m[1][0]*m[2][1]) - \
                  (m[0][2]*m[1][1]*m[2][0] + m[0][0]*m[1][2]*m[2][1] + m[0][1]*m[1][0]*m[2][2])
            self.resultado_area.insert(tk.END, f"\n\nDeterminante por Sarrus: {det:.2f}")
        else:
            messagebox.showerror("Error", "La matriz A debe ser 3x3.")

    def determinante(self, matriz):
        if len(matriz) == 2:
            return matriz[0][0]*matriz[1][1] - matriz[0][1]*matriz[1][0]
        det = 0
        for j in range(len(matriz)):
            submatriz = [fila[:j] + fila[j+1:] for fila in matriz[1:]]
            det += (-1)**j * matriz[0][j] * self.determinante(submatriz)
        return det

    def det_cofactores(self):
        if self.matriz_a:
            det = self.determinante(self.matriz_a)
            self.resultado_area.insert(tk.END, f"\n\nDeterminante por cofactores: {det:.2f}")
        else:
            messagebox.showinfo("Falta información", "Primero crea la matriz A.")

    def inversa(self):
        if self.matriz_a:
            try:
                inversa = np.linalg.inv(self.matriz_a).tolist()
                self.resultado_area.insert(tk.END, "\n\nMatriz Inversa de A:")
                self.mostrar_matriz(inversa, "A⁻¹")
            except:
                messagebox.showerror("Error", "La matriz no tiene inversa.")
        else:
            messagebox.showinfo("Falta información", "Primero crea la matriz A.")

def metodo_cramer(self):
    if self.matriz_a:
        try:
            coef = np.array(self.matriz_a)
            n = coef.shape[0]
            if coef.shape[0] != coef.shape[1]:
                messagebox.showerror("Error", "La matriz A debe ser cuadrada.")
                return

            constantes = [simpledialog.askfloat("Cramer", f"Ingrese el término independiente para la ecuación {i+1}:") for i in range(n)]
            b = np.array(constantes)

            det_a = round(np.linalg.det(coef), 4)
            self.resultado_area.insert(tk.END, f"\n\nDeterminante de A: {det_a:.4f}\n")

            if det_a == 0:
                self.resultado_area.insert(tk.END, "El sistema no tiene solución única (det(A) = 0)\n")
                return

            soluciones = []
            for i in range(n):
                matriz_modificada = np.copy(coef)
                matriz_modificada[:, i] = b
                det_i = round(np.linalg.det(matriz_modificada), 4)
                xi = det_i / det_a
                self.resultado_area.insert(tk.END, f"Determinante D{i+1} = {det_i:.4f}\n")
                soluciones.append(xi)

            for i, xi in enumerate(soluciones):
                self.resultado_area.insert(tk.END, f"x{i+1} = {xi:.4f}\n")

        except Exception as e:
            messagebox.showerror("Error", f"No se puede aplicar Cramer: {e}")
    else:
        messagebox.showinfo("Falta información", "Primero crea la matriz A.")

if __name__ == "__main__":
    root = tk.Tk()
    app = MatrizApp(root)
    root.mainloop()
