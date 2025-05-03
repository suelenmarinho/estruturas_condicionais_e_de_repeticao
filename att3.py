misseis = 5

naves_inimigas = ["Crazy-X", "Mega-Tronco", "S3Z"]

while misseis > 0 and naves_inimigas:
    print(f"\nMísseis restantes: {misseis}")
    print("Naves inimigas:")
    for idx, nave in enumerate(naves_inimigas):
        print(f"[{idx}] {nave}")

    try:
        escolha = int(input("Escolha o índice da nave para atacar: "))
        if escolha < 0 or escolha >= len(naves_inimigas):
            print("Índice inválido! Tente novamente.")
            continue
    except ValueError:
        print("Entrada inválida! Digite um número.")
        continue

    nave_destruida = naves_inimigas.pop(escolha)
    misseis -= 1
    print(f"Nave {nave_destruida} destruída!")

if not naves_inimigas:
    print("\nVitória! Todas as naves inimigas foram destruídas!")
elif misseis == 0:
    print("\nSem mísseis! Retirada estratégica!")
