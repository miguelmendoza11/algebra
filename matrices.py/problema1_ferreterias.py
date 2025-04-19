import tkinter as tk
from tkinter import messagebox

class FerreteriaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Problema 1: Ferreterías")
        
        self.resultado_area = tk.Text(root, width=80, height=20)
        self.resultado_area.pack(pady=10)
        
        btn_mostrar_matrices = tk.Button(root, text="Mostrar Matrices y Resultados", command=self.calcular)
        btn_mostrar_matrices.pack(pady=5)
        
        self.resultado_area.insert(tk.END, "Presiona el botón para mostrar las matrices y resultados...\n")

    def calcular(self):
        #productos y precios
        productos = ["Pintura", "Clavos", "Martillos"]
        precios_compra = [50, 55, 30]
        precios_venta = [56, 65, 36]
        matriz_precios = [precios_compra, precios_venta]
        
        #productos vendidos 
        matriz_ventas = [
            [30, 20, 69],  # Tienda 1
            [45, 29, 56]   # Tienda 2
        ]

        # Multiplicación de matrices (Precio x Venta Transpuesta)
        import numpy as np
        precios_np = np.array(matriz_precios)
        ventas_np = np.array(matriz_ventas)
        
        ventas_np_T = ventas_np.T  # Transpuesta para multiplicación compatible
        resultado = np.dot(precios_np, ventas_np_T)  # (2x3) x (3x2) = (2x2)
        
        self.resultado_area.delete(1.0, tk.END)
        self.resultado_area.insert(tk.END, "Matriz de precios (Compra y Venta):\n")
        for fila in matriz_precios:
            self.resultado_area.insert(tk.END, f"{fila}\n")

        self.resultado_area.insert(tk.END, "\nMatriz de ventas por tienda (productos):\n")
        for fila in matriz_ventas:
            self.resultado_area.insert(tk.END, f"{fila}\n")

        self.resultado_area.insert(tk.END, "\nResultado de la multiplicación (Total Compra/Venta):\n")
        self.resultado_area.insert(tk.END, "Filas: Compra/Venta | Columnas: Tienda 1, Tienda 2\n")
        self.resultado_area.insert(tk.END, f"{resultado}\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = FerreteriaApp(root)
    root.mainloop()
