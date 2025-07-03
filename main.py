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

        try:
            velocidade = float(input("Introduza a velocidade do veículo (km/h): "))
        except ValueError:
            print("Por favor, introduza um valor numérico para a velocidade.")
            continue

        
        print(f"Local escolhido: {loc}, Velocidade: {velocidade} km/h")
if __name__ == "__main__":
    main()
