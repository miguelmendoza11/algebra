
import tkinter as tk
import numpy as np

class VideoclubApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Problema 2: Videoclub")
        
        self.resultado_area = tk.Text(root, width=90, height=25)
        self.resultado_area.pack(pady=10)
        
        btn_resolver = tk.Button(root, text="Resolver sistema con Cramer", command=self.resolver)
        btn_resolver.pack(pady=5)

        self.resultado_area.insert(tk.END, "Presiona el botón para resolver el sistema de ecuaciones...\n")

    def resolver(self):
        # Variables: x = infantiles, y = oeste, z = terror
        # Sistema:
        # 0.6x + 0.5y + 0.3z = 1.0T
        # 0.2x + 0.6y + 0.6z = 0.5T
        # y = x + 100

        # Sustituimos y = x + 100 en las dos primeras ecuaciones
        # Ecuación 1: 0.6x + 0.5(x + 100) + 0.3z = T
        #             0.6x + 0.5x + 50 + 0.3z = T  → 1.1x + 0.3z = T - 50
        # Ecuación 2: 0.2x + 0.6(x + 100) + 0.6z = 0.5T
        #             0.2x + 0.6x + 60 + 0.6z = 0.5T  → 0.8x + 0.6z = 0.5T - 60

        
        # Sistema reducido con 2 ecuaciones y dos incógnitas (x y z)
        # Para resolverlo con Cramer, usamos coeficientes:
        A = np.array([[1.1, 0.3], [0.8, 0.6]])
        B = np.array([1.0 - 50/100, 0.5 - 60/100])  # Ya dividido T (lo tratamos como 100 para simplicidad)
        B = B * 100  # Tomamos T = 100

        #calcula determinantes
        D = np.linalg.det(A)
        Dx = np.linalg.det(np.array([[B[0], A[0][1]], [B[1], A[1][1]]]))
        Dz = np.linalg.det(np.array([[A[0][0], B[0]], [A[1][0], B[1]]]))

        #resultado
        x = Dx / D
        z = Dz / D
        y = x + 100

        self.resultado_area.delete(1.0, tk.END)
        self.resultado_area.insert(tk.END, "Sistema de ecuaciones transformado:\n")
        self.resultado_area.insert(tk.END, "1.1x + 0.3z = 50\n")
        self.resultado_area.insert(tk.END, "0.8x + 0.6z = -10\n")
        self.resultado_area.insert(tk.END, "Además: y = x + 100\n\n")
        
        self.resultado_area.insert(tk.END, f"Determinante D = {D:.2f}\n")
        self.resultado_area.insert(tk.END, f"Determinante Dx = {Dx:.2f}\n")
        self.resultado_area.insert(tk.END, f"Determinante Dz = {Dz:.2f}\n\n")

        self.resultado_area.insert(tk.END, f"Resultado:\n")
        
        #resultado interfaz grafica
        self.resultado_area.insert(tk.END, f"Películas infantiles (x) = {x:.2f}\n")
        self.resultado_area.insert(tk.END, f"Películas oeste (y) = {y:.2f}\n")
        self.resultado_area.insert(tk.END, f"Películas terror (z) = {z:.2f}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoclubApp(root)
    root.mainloop()
