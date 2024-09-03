# Paradigma Imperativo
def factorialImp(n):
    if n == 0:
        return 1
    else:
        return n * factorialImp(n - 1)

# Paradigma Funcional
from functools import reduce
def factorialFunc(n):
  return reduce(lambda x, y: x * y, range(1, n + 1))


opcion=1
while(opcion!=0):
  n=int(input("Ingree un numero para calcular factorial:"))
  print(factorialImp(n))
  print(factorialFunc(n))
  opcion=int(input("Pulse 0 para salir [Cualquier otro numero para continuar]"))
