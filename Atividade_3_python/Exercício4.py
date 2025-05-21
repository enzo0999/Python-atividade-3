while True:
    
    print("\nMenu:")
    print("[1] Olá")
    print("[2] Ajuda")
    print("[3] Sair")
    
    
    escolha = input("Escolha uma opção: ")


    if escolha == "1":
        print("\nOlá! Como você está?")
    elif escolha == "2":
        print("\nVocê escolheu a opção de ajuda. O que posso fazer por você?")
    elif escolha == "3":
        print("\nSaindo... Até logo!")
        break  
    else:
        print("\nOpção inválida. Tente novamente.")
