tup1 = (1, 2, 3)
print(tup1)
#tup1[0] = 0 # Tuplas sao imutaveis, uma vez criadas, nao podem ser modificadas.
# packing - unpacking
a, b = 0, 'Deu certo?!'
print(f'{a} \n {b}') # A recebeu 0 enquanto B 'Deu certo?!'
# Trocando valore de A e B
a, b = b, a
print(f'{a} \n {b}') # A = 'Deu certo?!', B = 0