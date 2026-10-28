import numpy as np

fallos = []
paginas = []
marcos=[]
contadores=[]
fallos=[]

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
matriz = np.zeros((numMarcos, numMarcos), dtype=int)

'''imprimir matriz
for i in range(numMarcos):
    for j in range(numMarcos):
        print(matriz[i][j], end=" ")
    print()'''

i=0
while i != numMarcos:
    contadores.append(0)
    i = i +1 
    


numPag=int(input('Numero de Páginas (minimo 5, maximo 16):'))


print('Introduzca el flujo (la demanda) de de páginas')
i = 0

while i!= numPag:
    x = int(input(f'Página {i+1}:'))
    i = i + 1
    paginas.append(x)
    
print(paginas)


while len(fallos) != numPag:
    for p in paginas:
        if p in marcos:
            """LRU"""
            imprimir()
        else:
            imprimir()
        
    
   


Aqui lo dejo por ahroa, en un rato o mañana antes de las 11 les paso el github