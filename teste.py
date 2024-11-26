from random import randint
import math
# import matplotlib.pyplot as plt

def gerar_angulo():
    vetor = [30, 45, 60]
    indice = randint(0, 2)
    return vetor[indice]

def gerar_velocidade():
    return randint(10, 100)

def calcular_altura_maxima(velocidade, angulo):
    angulo_rad = math.radians(angulo)
    return (pow(velocidade, 2) * pow(math.sin(angulo_rad), 2)) / (2 * 9.8)

def calcular_distancia(velocidade, angulo):
    angulo_rad = math.radians(angulo)
    return (pow(velocidade, 2) * math.sin(2 * angulo_rad)) / 9.8

def menu():
    op = ""
    while not op.isdigit() or int(op) < 0 or int(op) > 3:
        print("\nJOGO DE ADIVINHAÇÃO")
        print("1 - Adivinhar Distância")
        print("2 - Adivinhar Altura Máxima")
        print("3 - Plotar Trajetória")
        print("0 - Sair")
        op = input("Escolha sua opção: ")
    return int(op)

def plotar_trajetoria(velocidade, angulo):
    angulo_rad = math.radians(angulo)
    g = 9.8
    t_total = (2 * velocidade * math.sin(angulo_rad)) / g
    tempos = [t / 100 for t in range(int(t_total * 100) + 1)]
    x = [velocidade * math.cos(angulo_rad) * t for t in tempos]
    y = [(velocidade * math.sin(angulo_rad) * t) - (0.5 * g * t**2) for t in tempos]

    # plt.plot(x, y)
    # plt.title("Trajetória do Projétil")
    # plt.xlabel("Distância (m)")
    # plt.ylabel("Altura (m)")
    # plt.grid(True)
    # plt.show()

# Programa principal

velocidade = gerar_velocidade()
angulo = gerar_angulo()

print("Velocidade: %.2f" %velocidade)
print("Ângulo: %d°" %angulo)

distancia_real = calcular_distancia(velocidade, angulo)
altura_real = calcular_altura_maxima(velocidade, angulo)

pontos = 0
while True:
    opcao = menu()
    if opcao == 0:
        print("\nFim do jogo! Pontuação final:", pontos)
        break
    elif opcao == 1:
        print("\nAdivinhe a Distância")
        chute = float(input("Informe sua estimativa para a distância (em metros): "))
        erro = abs(chute - distancia_real)
        if erro < 1:
            print("Parabéns! Você acertou muito perto!")
            pontos += 10
        elif erro < 5:
            print("Quase lá! Você errou por pouco.")
            pontos += 5
        else:
            print(f"Errado! A distância real era {distancia_real:.2f} m.")
    elif opcao == 2:
        print("\nAdivinhe a Altura Máxima")
        chute = float(input("Informe sua estimativa para a altura máxima (em metros): "))
        erro = abs(chute - altura_real)
        if erro < 1:
            print("Parabéns! Você acertou muito perto!")
            pontos += 10
        elif erro < 3:
            print("Quase lá! Você errou por pouco.")
            pontos += 5
        else:
            print(f"Errado! A altura real era {altura_real:.2f} m.")
    elif opcao == 3:
        print("\nPlotando a trajetória do projétil...")
        plotar_trajetoria(velocidade, angulo)
    input("Pressione Enter para continuar...")


