import numpy as np

fallos = []
paginas = []
marcos=[]
contadores=[]

def agregar(x):
    if x == 0:
        fallos.append(' ')
    if x == 1:
        fallos.append('X')
        
def imprimir(x=0):
        print(f'Marcos: ', marcos)
        print(f'Matriz')
        for i in range(numMarcos):
            for j in range(numMarcos):
                print(matriz[i][j], end=" ")
            print()
        print(f'Contadores', contadores)
        agregar(x)
        print(f'Fallos', fallos)
             
print('ALGORITMO LRU PARA REEMPLAZO DE PÁGINAS\n')
numMarcos=int(input('Numero de Marcos (minimo 3, maximo 4):'))
while numMarcos < 3 or numMarcos > 4:
    print("Valor invalido. Debe ser entre 3 y 4.")
    numMarcos=int(input('Numero de Marcos (minimo 3, maximo 4):'))
    
matriz = np.zeros((numMarcos, numMarcos), dtype=int)

i=0
while i != numMarcos:
    contadores.append(0)
    i = i +1 

numPag=int(input('Numero de Páginas (minimo 5, maximo 16):'))
while numPag < 5 or numPag > 16:
    print("Valor invalido. Debe ser entre 5 y 16.")
    numPag=int(input('Numero de Páginas (minimo 5, maximo 16):'))


print('Introduzca el flujo (la demanda) de páginas')
for i in range(numPag):
    x = int(input(f'Página {i+1}: '))
    paginas.append(x)
print(paginas)

for p in paginas:
    print(f"\n--- Procesando página {p} ---")
    if p in marcos:
        """LRU"""
        imprimir()
    else:
        imprimir()
        
    
   