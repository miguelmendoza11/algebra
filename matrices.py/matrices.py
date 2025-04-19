
import numpy as np

class OperacionesMatrices:
    def __init__(self):
        pass
    
    def imprimir_matriz(self, matriz, nombre="Matriz"):
        print(f"\n{nombre}:")
        for fila in matriz:
            print(" ".join(f"{x:8.3f}" for x in fila))
    
    def crear_matriz(self, filas, columnas, mensaje="Ingrese los elementos de la matriz:"):
        print(mensaje)
        matriz = []
        for i in range(filas):
            fila = []
            for j in range(columnas):
                valor = float(input(f"Elemento [{i+1},{j+1}]: "))
                fila.append(valor)
            matriz.append(fila)
        return matriz
    
    def suma_matrices(self, matriz_a, matriz_b):
        if len(matriz_a) != len(matriz_b) or len(matriz_a[0]) != len(matriz_b[0]):
            return "Error: Las matrices deben tener las mismas dimensiones para sumarlas"
        
        return [[matriz_a[i][j] + matriz_b[i][j] for j in range(len(matriz_a[0]))] for i in range(len(matriz_a))]
    
    def multiplicacion_matrices(self, matriz_a, matriz_b):
        if len(matriz_a[0]) != len(matriz_b):
            return "Error: El número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz"
        
        return [[sum(matriz_a[i][k] * matriz_b[k][j] for k in range(len(matriz_a[0]))) for j in range(len(matriz_b[0]))] for i in range(len(matriz_a))]
    
    def determinante_sarrus(self, matriz):
        if len(matriz) != 3 or len(matriz[0]) != 3:
            return "Error: El método de Sarrus solo funciona para matrices 3x3"
        
        return (matriz[0][0] * matriz[1][1] * matriz[2][2] + matriz[0][1] * matriz[1][2] * matriz[2][0] + matriz[0][2] * matriz[1][0] * matriz[2][1]) - \
               (matriz[0][2] * matriz[1][1] * matriz[2][0] + matriz[0][0] * matriz[1][2] * matriz[2][1] + matriz[0][1] * matriz[1][0] * matriz[2][2])
    
    def determinante_cofactores(self, matriz):
        if len(matriz) == 2:
            return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
        
        return sum((-1) ** j * matriz[0][j] * self.determinante_cofactores([fila[:j] + fila[j+1:] for fila in matriz[1:]]) for j in range(len(matriz)))
    
    def matriz_inversa(self, matriz):
        det = self.determinante_cofactores(matriz)
        if abs(det) < 1e-10:
            return "Error: La matriz no tiene inversa (determinante = 0)"
        
        adjunta = [[(-1) ** (i+j) * self.determinante_cofactores([fila[:j] + fila[j+1:] for fila in matriz[:i] + matriz[i+1:]]) for j in range(len(matriz))] for i in range(len(matriz))]
        return [[adjunta[j][i] / det for j in range(len(matriz))] for i in range(len(matriz))]

    def metodo_cramer(self, matriz_coeficientes, vector_constantes):
        n = len(matriz_coeficientes)
        
        if any(len(fila) != n for fila in matriz_coeficientes) or len(vector_constantes) != n:
            return "Error: La matriz debe ser cuadrada y el vector de constantes debe tener la misma longitud"
        
        det_matriz = self.determinante_cofactores(matriz_coeficientes)
        if abs(det_matriz) < 1e-10:
            return "Error: El sistema no tiene solución única (determinante = 0)"
        
        soluciones = []
        for i in range(n):
            matriz_modificada = [fila[:] for fila in matriz_coeficientes]
            for j in range(n):
                matriz_modificada[j][i] = vector_constantes[j]
            det_modificada = self.determinante_cofactores(matriz_modificada)
            soluciones.append(det_modificada / det_matriz)
        
        return soluciones


def menu():
    print("Iniciando programa...")
    operaciones = OperacionesMatrices()
    matriz_a = None
    matriz_b = None
    
    while True:
        print("\n==== OPERACIONES CON MATRICES ====")
        print("1. Crear matriz A")
        print("2. Crear matriz B")
        print("3. Suma de matrices")
        print("4. Multiplicación de matrices")
        print("5. Determinante por Sarrus (matriz 3x3)")
        print("6. Determinante por cofactores")
        print("7. Matriz inversa")
        print("8. Resolver sistema con método de Cramer")
        print("0. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            filas = int(input("Número de filas para matriz A: "))
            columnas = int(input("Número de columnas para matriz A: "))
            matriz_a = operaciones.crear_matriz(filas, columnas, "Ingrese los elementos de la matriz A:")
            operaciones.imprimir_matriz(matriz_a, "Matriz A")
        
        elif opcion == "2":
            filas = int(input("Número de filas para matriz B: "))
            columnas = int(input("Número de columnas para matriz B: "))
            matriz_b = operaciones.crear_matriz(filas, columnas, "Ingrese los elementos de la matriz B:")
            operaciones.imprimir_matriz(matriz_b, "Matriz B")
        
        elif opcion == "3":
            if matriz_a is None or matriz_b is None:
                print("Error: Primero debe crear ambas matrices")
                continue
            resultado = operaciones.suma_matrices(matriz_a, matriz_b)
            operaciones.imprimir_matriz(resultado, "Resultado de la suma")
        
        elif opcion == "4":
            if matriz_a is None or matriz_b is None:
                print("Error: Primero debe crear ambas matrices")
                continue
            resultado = operaciones.multiplicacion_matrices(matriz_a, matriz_b)
            operaciones.imprimir_matriz(resultado, "Resultado de la multiplicación")
        
        elif opcion == "5":
            if matriz_a is None:
                print("Error: Primero debe crear la matriz A")
                continue
            print(f"\nDeterminante (Sarrus): {operaciones.determinante_sarrus(matriz_a)}")
        
        elif opcion == "6":
            if matriz_a is None:
                print("Error: Primero debe crear la matriz A")
                continue
            print(f"\nDeterminante (Cofactores): {operaciones.determinante_cofactores(matriz_a)}")
        
        elif opcion == "7":
            if matriz_a is None:
                print("Error: Primero debe crear la matriz A")
                continue
            resultado = operaciones.matriz_inversa(matriz_a)
            if isinstance(resultado, str): 
                print(resultado)
            else:
                operaciones.imprimir_matriz(resultado, "Matriz Inversa")

        elif opcion == "8":
            n = int(input("Ingrese el número de incógnitas (n): "))
            print("Ingrese los coeficientes del sistema (matriz A):")
            matriz_coef = operaciones.crear_matriz(n, n)
            print("Ingrese el vector de constantes (vector B):")
            vector_b = []
            for i in range(n):
                valor = float(input(f"Elemento [{i+1}]: "))
                vector_b.append(valor)
            
            resultado = operaciones.metodo_cramer(matriz_coef, vector_b)
            if isinstance(resultado, str):
                print(resultado)
            else:
                print("\nSoluciones del sistema:")
                for idx, valor in enumerate(resultado):
                    print(f"x{idx+1} = {valor:.5f}")

        elif opcion == "0":
            print("¡Gracias por usar el programa!")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
