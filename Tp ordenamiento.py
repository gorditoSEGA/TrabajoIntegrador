import time
import random

# ----------------------------------------
# Algoritmos de ordenamiento y búsqueda
# ----------------------------------------

# ----------- ORDENAMIENTOS -----------

def ordenamiento_burbuja(arr):
    comparaciones = intercambios = 0
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            comparaciones += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                intercambios += 1
    return arr, comparaciones, intercambios


def ordenamiento_insercion(arr):
    comparaciones = intercambios = 0
    for i in range(1, len(arr)):
        clave = arr[i]
        j = i - 1
        while j >= 0 and clave < arr[j]:
            comparaciones += 1
            arr[j + 1] = arr[j]
            j -= 1
            intercambios += 1
        arr[j + 1] = clave
    return arr, comparaciones, intercambios


def quicksort(arr):
    """
    Implementación básica de quicksort sin contadores.
    """
    if len(arr) <= 1:
        return arr
    else:
        pivote = arr[0]
        menores = [x for x in arr[1:] if x <= pivote]
        mayores = [x for x in arr[1:] if x > pivote]
        return quicksort(menores) + [pivote] + quicksort(mayores)


# ----------- BÚSQUEDAS -----------

def busqueda_lineal(arr, objetivo):
    for i in range(len(arr)):
        if arr[i] == objetivo:
            return i
    return -1


def busqueda_binaria(arr, objetivo):
    izquierda = 0
    derecha = len(arr) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if arr[medio] == objetivo:
            return medio
        elif arr[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1


# ----------- PRUEBAS -----------

def probar_ordenamientos(lista):
    print("Original:", lista)

    print("\n--- Burbuja ---")
    inicio = time.time()
    ordenada, comp, interc = ordenamiento_burbuja(lista.copy())
    fin = time.time()
    print("Ordenada:", ordenada)
    print(f"Comparaciones: {comp}, Intercambios: {interc}, Tiempo: {round(fin - inicio, 5)}s")

    print("\n--- Inserción ---")
    inicio = time.time()
    ordenada, comp, interc = ordenamiento_insercion(lista.copy())
    fin = time.time()
    print("Ordenada:", ordenada)
    print(f"Comparaciones: {comp}, Intercambios: {interc}, Tiempo: {round(fin - inicio, 5)}s")

    print("\n--- Quicksort ---")
    inicio = time.time()
    ordenada = quicksort(lista.copy())
    fin = time.time()
    print("Ordenada:", ordenada)
    print(f"Tiempo: {round(fin - inicio, 5)}s (No cuenta comparaciones ni intercambios)\n")


def probar_busquedas(lista, objetivo):
    print("Lista ordenada:", lista)
    print(f"Buscando el número {objetivo}...")

    pos_lin = busqueda_lineal(lista, objetivo)
    print(f"Búsqueda lineal: Posición {pos_lin}" if pos_lin != -1 else "No encontrado (lineal)")

    pos_bin = busqueda_binaria(lista, objetivo)
    print(f"Búsqueda binaria: Posición {pos_bin}" if pos_bin != -1 else "No encontrado (binaria)")


# ----------- MAIN -----------

def main():
    # Listas para probar
    chica = [12, 5, 9, 1, 6]
    mediana = random.sample(range(1, 100), 20)
    grande = random.sample(range(1, 1000), 100)

    print("\n====== Lista chica ======")
    probar_ordenamientos(chica)
    probar_busquedas(sorted(chica), 6)

    print("\n====== Lista mediana ======")
    probar_ordenamientos(mediana)
    probar_busquedas(sorted(mediana), 50)

    print("\n====== Lista grande ======")
    probar_ordenamientos(grande)
    probar_busquedas(sorted(grande), 123)


if __name__ == "__main__":
    main()













#----- PRUEBA PRACTICA -----

import time
import random
import matplotlib.pyplot as plt


def medir_tiempo_ordenamiento(funcion, lista):
    """Mide cuánto tarda un algoritmo de ordenamiento"""
    inicio = time.time()
    funcion(lista.copy())
    fin = time.time()
    return round(fin - inicio, 5)


def medir_tiempo_busqueda(funcion, lista, objetivo, repeticiones=10000):
    inicio = time.perf_counter()
    for _ in range(repeticiones):
        funcion(lista, objetivo)
    fin = time.perf_counter()
    tiempo_total = fin - inicio
    return round(tiempo_total / repeticiones, 8)


def analisis_rendimiento():
    tamaños = [10, 100, 1000, 3000, 5000, 7000, 10000]
    tiempos_burbuja = []
    tiempos_insercion = []
    tiempos_quick = []

    tiempos_lineal = []
    tiempos_binaria = []

    for n in tamaños:
        lista = random.sample(range(n * 2), n)
        objetivo = lista[n // 2]
        lista_ordenada = sorted(lista)

        print(f"Analizando tamaño {n}...")

        # Ordenamientos
        tiempos_burbuja.append(medir_tiempo_ordenamiento(ordenamiento_burbuja, lista))
        tiempos_insercion.append(medir_tiempo_ordenamiento(ordenamiento_insercion, lista))
        tiempos_quick.append(medir_tiempo_ordenamiento(quicksort, lista))

        # Búsquedas (usamos lista ordenada para binaria)
        tiempos_lineal.append(medir_tiempo_busqueda(busqueda_lineal, lista_ordenada, objetivo))
        tiempos_binaria.append(medir_tiempo_busqueda(busqueda_binaria, lista_ordenada, objetivo))

    # Visualización
    plt.figure(figsize=(12, 6))

    # Gráfico de ordenamientos
    plt.subplot(1, 2, 1)
    plt.plot(tamaños, tiempos_burbuja, label="Burbuja", marker='o')
    plt.plot(tamaños, tiempos_insercion, label="Inserción", marker='o')
    plt.plot(tamaños, tiempos_quick, label="Quicksort", marker='o')
    plt.title("Tiempo de ordenamiento según el tamaño")
    plt.xlabel("Cantidad de elementos")
    plt.ylabel("Tiempo (segundos)")
    plt.legend()
    plt.grid(True)

    # Gráfico de búsquedas
    plt.subplot(1, 2, 2)
    plt.plot(tamaños, tiempos_lineal, label="Lineal", marker='o')
    plt.plot(tamaños, tiempos_binaria, label="Binaria", marker='o')
    plt.title("Tiempo de búsqueda según el tamaño")
    plt.xlabel("Cantidad de elementos")
    plt.ylabel("Tiempo (segundos)")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()






#Ejemplo busqueda lineal para la diapositiva

#lista = [5, 3, 8, 1, 9]
#objetivo = 8

# Recorre toda la lista hasta encontrarlo
#for i in range(len(lista)):
   # if lista[i] == objetivo:
     #   print(f"Encontrado en la posición {i}")
      #  break





#ejemplo busqueda binaria para la diapositiva

#lista = [1, 3, 5, 8, 9]  # La lista debe estar ORDENADA
#objetivo = 8

#izq = 0
#der = len(lista) - 1

#while izq <= der:
  #  medio = (izq + der) // 2
  #  if lista[medio] == objetivo:
   #     print(f"Encontrado en la posición {medio}")
   #     break
   # elif lista[medio] < objetivo:
   #     izq = medio + 1
   # else:
    #    der = medio - 1
