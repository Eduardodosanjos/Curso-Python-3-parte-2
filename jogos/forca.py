def jogar():
    print("*********************************")
    print("***Bem Vindo ao Jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana"
    enforcou = False
    acertou = False

    while not enforcou and not acertou:
        chute = input("Qual letra? ")

        index = 0
        for letra in palavra_secreta:
            if chute == letra:
                print(f'Encontrei a letra {chute} na prosição {index}')
            index += 1

    print("Fim do Jogo")

if __name__ == "__main__":
    jogar()