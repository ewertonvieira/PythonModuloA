palavra = 'Termodinamica'
print(palavra[2])
print(2*palavra[0]) # 2 * Palavra reotnra duas vezes a posicao 0
print(palavra[0:13]) # Retorna o intervalo 0 a 13; Lembrando que os valores estao entre as letras
print(palavra[9:]) # Entende 9: como espaco 9 ate o fim que é 13
print(palavra[:9]) # Primeiro endereço ate o 9)
print(palavra[0:9])
print(palavra[:]) # Com : obtermos toda a palavra
print(palavra[1:8]) # Intervalo de 1 a 8
print(palavra[1:8:2]) # Obteremos 1:8:2, de 1 a 8, com incremento de 2: 1, 3, 5, 7
print(palavra[1:8:3]) # Agora incrementando 3: 1, 4, 7
print(palavra[7:0: -1]) # Decrementa 7 com -1: 7, 6, 5, 4, 3, 2, 1, 0 | Varre a palavra na ordem invertida
print(palavra[:4:-2]) # Vai de 0 -2 inversamente ate 4: -1, -3, - 5
print(palavra[::-1]) # Decrementa -1 apartir do 0: 0, -1, -2, -3 ...-13
palindromo = 'socorrem me subi no onibus em marrocos'
print(palindromo[::-1]) # Leitura invertida.
