lista = [1, 2, 3]
print(lista) # IMprime lista
print(lista[0] + lista[2]) # Somando espaco lista[0] = 1, com lsita[2] = 3, ou seja Saida: 4
#print(lista + 4) dara erro pois esta tentando cocatenar lista 4 a uma lista [1, 2, 3]
lista = lista + [4] # soma lista [1, 2, 3] a [4]; resultando em [1, 2, 3, 4] 
print(lista)
lista = lista + [0, 0, 0] # resulta em lista [1, 2, 3, 0, 0, 0]
print(lista)
print(lista[-1])
print(lista[2: -2]) # decrementa 2, ate -4.
lista[0] = 'Zero'# Add 'Zero' ao espaco 0
print(lista)
lista[2] = lista[0] # Espaco 2 receve zero do espaco 0;
print(lista)
 # Strings
#a = 'Boa tarde!'
#a[0] = 'N' 
print("##########################################")
linha1 = [1, 2, 3]; linha2 = [0, -1,1]; linha3 = [3, 3, 3]
matriz = [linha1, linha2, linha3]
print(matriz)
print(matriz[1] [2])