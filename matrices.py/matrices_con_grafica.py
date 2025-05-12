
import tkinter as tk
from tkinter import simpledialog, messagebox, scrolledtext
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class MatrizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Operaciones con Matrices y Vectores")
        
        self.matriz_a = None
        self.matriz_b = None
        self.vector_a = None
        self.vector_b = None

        tk.Label(root, text="Operaciones con Matrices y Vectores", font=("Helvetica", 16, "bold")).pack(pady=10)
        
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
            ("Método de Cramer", self.metodo_cramer),
            ("Crear Vector A", self.crear_vector_a),
            ("Crear Vector B", self.crear_vector_b),
            ("Suma de Vectores", self.suma_vectores),
            ("Resta de Vectores", self.resta_vectores),
            ("Escalar por Vector A", self.escalar_por_vector),
            ("Producto Punto", self.producto_punto),
            ("Producto Cruz", self.producto_cruz),
            ("Magnitud y Dirección", self.magnitud_direccion),
            ("Graficar Vectores", self.graficar_vectores),
("Transformación Cero", self.transformacion_cero),
            ("Transformación Identidad", self.transformacion_identidad),
            ("Reflexión eje X", self.reflexion_eje_x),
            ("Reflexión eje Y", self.reflexion_eje_y),
            ("Rotación", self.rotacion),
            ("Escala", self.escalamiento),
            ("Traslación", self.traslacion),
        ]

        for texto, comando in botones:
            tk.Button(btn_frame, text=texto, width=25, command=comando).pack(pady=2)
        
        self.resultado_area = scrolledtext.ScrolledText(root, width=80, height=20)
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

    # ==== VECTORES ====

    def crear_vector_a(self):
        longitud = simpledialog.askinteger("Vector A", "Ingrese la dimensión del vector A:")
        self.vector_a = np.array([simpledialog.askfloat("Vector A", f"A[{i+1}] = ") for i in range(longitud)])
        self.resultado_area.insert(tk.END, f"\nVector A: {self.vector_a}\n")

    def crear_vector_b(self):
        longitud = simpledialog.askinteger("Vector B", "Ingrese la dimensión del vector B:")
        self.vector_b = np.array([simpledialog.askfloat("Vector B", f"B[{i+1}] = ") for i in range(longitud)])
        self.resultado_area.insert(tk.END, f"\nVector B: {self.vector_b}\n")

    def suma_vectores(self):
        if self.vector_a is not None and self.vector_b is not None:
            resultado = self.vector_a + self.vector_b
            self.resultado_area.insert(tk.END, f"\nA + B = {resultado}\n")
        else:
            messagebox.showinfo("Falta información", "Primero define los vectores A y B.")

    def resta_vectores(self):
        if self.vector_a is not None and self.vector_b is not None:
            resultado = self.vector_a - self.vector_b
            self.resultado_area.insert(tk.END, f"\nA - B = {resultado}\n")
        else:
            messagebox.showinfo("Falta información", "Primero define los vectores A y B.")

    def escalar_por_vector(self):
        if self.vector_a is not None:
            escalar = simpledialog.askfloat("Escalar", "Ingrese el escalar a multiplicar por A:")
            resultado = escalar * self.vector_a
            self.resultado_area.insert(tk.END, f"\n{escalar} * A = {resultado}\n")
        else:
            messagebox.showinfo("Falta información", "Primero define el vector A.")

    def producto_punto(self):
        if self.vector_a is not None and self.vector_b is not None:
            resultado = np.dot(self.vector_a, self.vector_b)
            self.resultado_area.insert(tk.END, f"\nA · B = {resultado}\n")
        else:
            messagebox.showinfo("Falta información", "Primero define los vectores A y B.")

    def producto_cruz(self):
        if self.vector_a is not None and self.vector_b is not None and len(self.vector_a) == 3 and len(self.vector_b) == 3:
            resultado = np.cross(self.vector_a, self.vector_b)
            self.resultado_area.insert(tk.END, f"\nA × B = {resultado}\n")
        else:
            messagebox.showinfo("Error", "Los vectores deben ser de dimensión 3.")

    def magnitud_direccion(self):
        if self.vector_a is not None:
            magnitud = np.linalg.norm(self.vector_a)
            direccion = self.vector_a / magnitud if magnitud != 0 else "No definida"
            self.resultado_area.insert(tk.END, f"\n||A|| = {magnitud:.4f}, Dirección = {direccion}\n")
        else:
            messagebox.showinfo("Falta información", "Primero define el vector A.")

    
    
    def graficar_vectores(self):
        if self.vector_a is not None:
            plt.figure()
            ax = plt.gca()
            ax.axhline(0, color='black', linewidth=1)
            ax.axvline(0, color='black', linewidth=1)
            ax.grid(True, which='both', linestyle='--', linewidth=0.5)

            # Dibujar Vector A
            ax.quiver(0, 0, self.vector_a[0], self.vector_a[1], angles='xy', scale_units='xy', scale=1, color='r', label='Vector A')
            ax.plot(self.vector_a[0], self.vector_a[1], 'ro')  # Punto final de Vector A
            ax.text(self.vector_a[0], self.vector_a[1], f" A({self.vector_a[0]}, {self.vector_a[1]})", color='r')

            if self.vector_b is not None:
                ax.quiver(0, 0, self.vector_b[0], self.vector_b[1], angles='xy', scale_units='xy', scale=1, color='b', label='Vector B')
                ax.plot(self.vector_b[0], self.vector_b[1], 'bo')  # Punto final de Vector B
                ax.text(self.vector_b[0], self.vector_b[1], f" B({self.vector_b[0]}, {self.vector_b[1]})", color='b')

            todos = [self.vector_a]
            if self.vector_b is not None:
                todos.append(self.vector_b)

            # Calcular límites dinámicos
            limites = np.max(np.abs(todos)) + 2
            ax.set_xlim(-limites, limites)
            ax.set_ylim(-limites, limites)

            ax.set_aspect('equal')
            ax.set_xlabel("Eje X")
            ax.set_ylabel("Eje Y")
            plt.title('Plano cartesiano con vectores y puntos finales')
            plt.legend()
            plt.show()
        else:
            messagebox.showinfo("Falta información", "Debe al menos definir el vector A.")




    def transformacion_cero(self):
        if self.vector_a is not None:
            transformado = np.array([0, 0])
            self._graficar_transformacion(self.vector_a, transformado, "Transformación Cero")
        else:
            messagebox.showinfo("Falta información", "Primero define el vector A.")

    def transformacion_identidad(self):
        if self.vector_a is not None:
            transformado = self.vector_a.copy()
            self._graficar_transformacion(self.vector_a, transformado, "Transformación Identidad")
        else:
            messagebox.showinfo("Falta información", "Primero define el vector A.")

    def reflexion_eje_x(self):
        if self.vector_a is not None:
            transformado = np.array([self.vector_a[0], -self.vector_a[1]])
            self._graficar_transformacion(self.vector_a, transformado, "Reflexión sobre eje X")
        else:
            messagebox.showinfo("Falta información", "Primero define el vector A.")

    def reflexion_eje_y(self):
        if self.vector_a is not None:
            transformado = np.array([-self.vector_a[0], self.vector_a[1]])
            self._graficar_transformacion(self.vector_a, transformado, "Reflexión sobre eje Y")
        else:
            messagebox.showinfo("Falta información", "Primero define el vector A.")

    def rotacion(self):
        if self.vector_a is not None:
            angulo = simpledialog.askfloat("Rotación", "Ingrese el ángulo de rotación (grados antihorario):")
            rad = np.radians(angulo)
            rot_matrix = np.array([[np.cos(rad), -np.sin(rad)], [np.sin(rad), np.cos(rad)]])
            transformado = rot_matrix @ self.vector_a
            self._graficar_transformacion(self.vector_a, transformado, f"Rotación de {angulo}°")
        else:
            messagebox.showinfo("Falta información", "Primero define el vector A.")

    def escalamiento(self):
        if self.vector_a is not None:
            esc_x = simpledialog.askfloat("Escalamiento", "Ingrese el factor de escala en X:")
            esc_y = simpledialog.askfloat("Escalamiento", "Ingrese el factor de escala en Y:")
            esc_matrix = np.array([[esc_x, 0], [0, esc_y]])
            transformado = esc_matrix @ self.vector_a
            self._graficar_transformacion(self.vector_a, transformado, "Transformación de Escala")
        else:
            messagebox.showinfo("Falta información", "Primero define el vector A.")

    def traslacion(self):
        if self.vector_a is not None:
            dx = simpledialog.askfloat("Traslación", "Ingrese el desplazamiento en X:")
            dy = simpledialog.askfloat("Traslación", "Ingrese el desplazamiento en Y:")
            transformado = self.vector_a + np.array([dx, dy])
            self._graficar_transformacion(self.vector_a, transformado, "Traslación")
        else:
            messagebox.showinfo("Falta información", "Primero define el vector A.")

    def _graficar_transformacion(self, original, transformado, titulo):
        plt.figure()
        ax = plt.gca()
        ax.axhline(0, color='black', linewidth=1)
        ax.axvline(0, color='black', linewidth=1)
        ax.grid(True, which='both', linestyle='--', linewidth=0.5)

        ax.quiver(0, 0, original[0], original[1], angles='xy', scale_units='xy', scale=1, color='r', label='Vector Original')
        ax.plot(original[0], original[1], 'ro')
        ax.text(original[0], original[1], f" A({original[0]:.2f}, {original[1]:.2f})", color='r')

        ax.quiver(0, 0, transformado[0], transformado[1], angles='xy', scale_units='xy', scale=1, color='g', label='Transformado')
        ax.plot(transformado[0], transformado[1], 'go')
        ax.text(transformado[0], transformado[1], f" T({transformado[0]:.2f}, {transformado[1]:.2f})", color='g')

        limites = np.max(np.abs([original, transformado])) + 2
        ax.set_xlim(-limites, limites)
        ax.set_ylim(-limites, limites)

        ax.set_aspect('equal')
        ax.set_xlabel("Eje X")
        ax.set_ylabel("Eje Y")
        plt.title(titulo)
        plt.legend()
        plt.show()


    

if __name__ == "__main__":
    root = tk.Tk()
    app = MatrizApp(root)
    root.mainloop()

