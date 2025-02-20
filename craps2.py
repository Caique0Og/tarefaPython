import random

print("Vamos começar!")
ponto = None
print("Jogador está jogando...")
dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
soma = dado1 + dado2
print(f"Jogador tirou {dado1} e {dado2} = {soma}")

if soma == 7 or soma == 11:
    print("Jogador ganhou!")
    ponto = soma

elif soma == 2 or soma == 3 or soma == 12:
    print("Jogador perdeu!")
    pontor = 0

else:
    print("Jogador está na fase de ponto!")
    ponto = soma
    while True:
        dado3 = random.randint(1, 6)
        dado4 = random.randint(1, 6)
        ponto2 = dado3 + dado4
        print(f"Jogador tirou {dado3} e {dado4} = {ponto2 }")
        if ponto2  == ponto:
            print("Jogador ganhou (segunda rolagem)!")
            break
        elif ponto2 == 7:
            print("Jogador perdeu! (segunda rolagem)")
            ponto = 0
            break

print("Jogo finalizado!")
