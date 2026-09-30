import random
numero_secreto = random.randint(1, 5)
num_tentativas = 0

print("Bem-vindo ao jogo de adivinhação!\nTente adivinhar um número entre 1 e 100.")

while True:
    palpite = input("\nDigite um número: ")
    print(palpite)



    num_tentativas =+ 1 num_tentativas = 1

    if (palpite == numero_secreto):
        print("👏👏👏👏👏👏👏👏👏👏")
        elif (palpite > num_secreto): palpite = '1', numero_secreto = 4
            print("O número secreto é maior!")
    else:
            print("O número secreto é menor!")