import random


def jogar():
    print("************************************")
    print("* Bem Vindo ao Jogo da Adivinhacao *")
    print("************************************")

    numero_secreto = random.randrange(1,101)
    #print(numero_secreto)
    total_tentativas = 0
    pontos = int(1000)


    print ("qual o nivel de dificuldade?")
    print("(1) - Fácil   (2) - Médio   (3) - Difífil")
    nivel = int(input("Digite sua escolha: "))

    if (nivel ==1):
        total_tentativas = 20
    elif (nivel == 2):
        total_tentativas = 10
    elif (nivel == 3):
        total_tentativas = 5
    else:
        print("número invalido.")



    for rodada in range (1,total_tentativas+1):
        print("tentativa {} de {}".format(rodada,total_tentativas))
        chute = int(input("Digite um número entre 1 e 100: "))

        if(chute < 0 or chute > 100):
            print("O número deve ser entre 1 e 100")
            continue

        print("você digitou {}".format(chute))

        if (numero_secreto == chute):
            print("Voce acertou")
            break
        else:
            pontos = pontos - chute
            if (chute > numero_secreto):
                print("você errou, chutou pra cima")
            else:
                print("você errou, chutou pra baixo")

    print("sua pontuação ficou: ",pontos)

    print("fim do jogo")

if(__name__== "__main__"):
    jogar()