import numpy as np

from time import time
inicio = time()
lista1 = list(range(10**8))
soma1 = 0

for i in lista1:
    soma1 += i    
fim = time()

tempo1 = fim - inicio
print(tempo1)

inicio2 = time()

array1 = np.array(lista1, dtype=float)
soma2 = array1.sum()


fim2 = time()

tempo2 = fim2 - inicio2
print(tempo2)