import random

numeros_aleatorios = [random.randint(1, 1000) for _ in range(100)]

pares = [num for num in numeros_aleatorios if num % 2 == 0]
impares = [num for num in numeros_aleatorios if num % 2 != 0]

print("Lista de números pares:", pares)
print("Tamaño de la lista:", len(pares))

print("Lista de números impares:", impares)
print("Tamaño de la lista:", len(impares))
