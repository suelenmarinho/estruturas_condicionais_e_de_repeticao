import random

d_segura = 6

while True:
    d_asteroide = random.randint(1, 10)
    print(f"Distância do asteroide: {d_asteroide}")

    if d_asteroide < 3:
        print("PERIGO! Asteroide muito próximo!")
        break
    elif d_asteroide < d_segura / 2:
        print("Aproximando-se de asteroide!")

    d_segura += 2

    if d_asteroide >= d_segura:   
        print("Navegação concluída com segurança!")
        break
