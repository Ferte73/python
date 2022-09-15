#Meu primeiro projeto sério
#.append
#.remove
#.pop
#.insert
#.sort()
#.clear

lista1 = []
Q = len(lista1)

print("CENTRAL DE PROBLEMAS")

while True:
    print("1. Adicione reclamação\n2. Veja as suas reclamações\n3. Retire reclamações\n4. Desfazer última ação\n5. Colocar a likta em ordem alfabética\n6. Sair")
    numero = input()

    if numero == "1":
        elemento = input("Qual o problema que deseja reportar?")
        lista1.append(elemento)
        continue

    elif numero == "2":
        for i in lista1:
            print(i)
        continue

    elif numero == "3":
        resposta = input("Digite o número de 0 a " + str(Q - 1) + " do problema a retirar" )
        try:
            resposta = int(resposta)
        except:
            print("Apenas responda com numeros inteiros entre 0 a " + str(Q - 1))
        lista1.pop(resposta)  
        continue 
    
    elif numero == "4":
        lista1.pop()
        continue
    
    elif numero == "5":
        lista1 = sorted(lista1)
        for i in lista1:
            print(i)
            continue
    
    elif numero == "6":
        break

    else:
        print("Opção inválida")
        break
