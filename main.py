def main():
    while True:
        print("\nOnde circulava o veículo?")
        print("Escolha uma opção:")
        print("1 Localidade")
        print("2 Fora da localidade")
        print("3 Autoestrada")
        print("4 Sair")
        print()

        try:
            loc = int(input("Introduza o local: "))
        except ValueError:
            print("Por favor, introduza um número válido.")
            continue

        if loc == 4:
            print("Programa encerrado.")
            break

        if loc not in [1, 2, 3]:
            print("Opção inválida. Tente novamente.")
            continue

        # Aqui depois vamos pedir a velocidade e calcular multa

if __name__ == "__main__":
    main()
