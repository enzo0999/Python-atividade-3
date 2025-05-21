X = int(input("Digite um número inteiro positivo: "))

if X > 0:  
    while X >= 0:
        print(X)
        X -= 1  
else:
    print("Por favor, digite um número positivo!")
