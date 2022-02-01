import forca
import adivinhacao


def escolhe_jogo():
    print("****************")
    print("escolha seu jogo")
    print("****************")

    print("(1) - Forca   (2) - Adivinhação")

    jogo = int(input("Sua escolha: "))

    if (jogo ==1):
        print("Iniciando Forca")
        forca.jogar()
    elif (jogo ==2):
        print("Iniciando Adivinhação")
        adivinhacao.jogar()

if(__name__== "__main__"):
    escolhe_jogo()