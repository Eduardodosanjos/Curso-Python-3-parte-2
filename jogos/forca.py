import random

def jogar():
    print("*********************************")
    print("***Bem Vindo ao Jogo da Forca!***")
    print("*********************************")

    arquivo = open("palavra.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while not enforcou and not acertou:
        chute = input("Qual letra? ")
        # Tirando os possíveis espaços em brancos
        chute = chute.strip().upper()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        print("Você Ganhou!!")
    else:
        print("Você Perdeu!!")

    print("Fim do Jogo")


if __name__ == "__main__":
    jogar()
