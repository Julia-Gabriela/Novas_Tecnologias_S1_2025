import random

num_secreto = random.randint(1,100)
tentativas = 0

print("Tente advinhar o número de 1 a 100:")

while True:
    palpite = int(input("Digite seu palpite:"))
    tentativas += 1

    if palpite == num_secreto:
        print("Parabéns, vc acertou!!")
        break
    elif palpite > num_secreto:
        print("Palpite alto!")
    elif palpite < num_secreto:
        print("Palpite baixo!")
    if tentativas == 10:
        break

