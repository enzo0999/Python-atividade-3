numeros = []
for i in range(3):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(numero)

numeros_multiplicados = [num * 2 for num in numeros]

print("Lista dos números originais:", numeros)
print("Lista dos números multiplicados por 2:", numeros_multiplicados)

soma_numeros = sum(numeros)
print("Soma dos números originais:", soma_numeros)

soma_multiplicados = sum(numeros_multiplicados)
print("Soma dos números multiplicados por 2:", soma_multiplicados)
