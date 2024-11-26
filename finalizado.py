import json
import math
import os
from random import randint
from time import sleep
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# Funções auxiliares
def gerar_angulo():
    return [30, 45, 60][randint(0, 2)]

def gerar_velocidade():
    return randint(10, 100)

def calcular_altura_maxima(velocidade, angulo):
    angulo_rad = math.radians(angulo)
    return (pow(velocidade, 2) * pow(math.sin(angulo_rad), 2)) / (2 * 9.8)

def calcular_distancia(velocidade, angulo):
    angulo_rad = math.radians(angulo)
    return (pow(velocidade, 2) * math.sin(2 * angulo_rad)) / 9.8

def calcular_pontos(pontoMaximo, chute, valor_real):
    erro = abs(chute - valor_real)
    fator_proximidade = math.exp(-erro / valor_real)
    pontos = int(pontoMaximo * fator_proximidade)
    print(f"🎯 Você ganhou: {pontos} pontos!\n")
    return pontos


# Funções do jogo
def menu():
    op = ""
    while not op.isdigit() or int(op) not in range(3):
        print("\n🎮 JOGO DE ADIVINHAÇÃO 🎮")
        print("1 - Adivinhar Distância")
        print("2 - Adivinhar Altura Máxima")
        op = input("\nEscolha sua opção: ")
    return int(op)

def boas_vindas():
    os.system("cls" if os.name == "nt" else "clear")
    print("🎉 Bem-vindo ao JOJULO 🎉")
    sleep(2)
    nome = obter_nome()
    os.system("cls" if os.name == "nt" else "clear")
    print(f"Olá, {nome}! Vamos começar o jogo. Boa sorte! 🎯\n")
    sleep(2)
    return nome

def obter_nome():
    nome = input("Por favor, informe o seu nome: ").strip()
    while len(nome) < 3:
        print("⚠️ Nome inválido! O nome deve ter pelo menos 3 caracteres.")
        nome = input("Informe o seu nome: ").strip()
    return nome

def iniciar_contagem():
    print("\nPrepare-se! O jogo começará em:")
    for i in range(3, 0, -1):
        print(f"{i}...")
        sleep(1)
    print("🎯 Valendo!\n")

def adivinha_distancia():
    pontos = 0
    iniciar_contagem()

    for i in range(3):
        pontoMaximo = 100
        velocidade = gerar_velocidade()
        angulo = gerar_angulo()
        distancia_real = int(calcular_distancia(velocidade, angulo))

        print(f"\n🔢 Tentativa {i + 1} de 3:")
        print(f"Velocidade: {velocidade} m/s | Ângulo: {angulo}°")
        print("💡 DICA: Digite -1 para exibir o gráfico da trajetória, mas a pontuação valerá apenas 50%!")
        chute = int(input("Qual a sua estimativa para a distância (em metros)? "))

        if chute == -1:
            plotar_trajetoria(velocidade, angulo)
            pontoMaximo = pontoMaximo / 2
            chute = int(input("Qual a sua estimativa para a distância (em metros)? "))

        if chute == distancia_real:
            print("✅ Parabéns! Você acertou!")
        else:
            print(f"❌ Errou! A distância correta era: {distancia_real} m.")
        pontos += calcular_pontos(pontoMaximo, chute, distancia_real)

    return pontos

def adivinha_altura():
    pontos = 0
    iniciar_contagem()

    for i in range(3):
        pontoMaximo = 100
        velocidade = gerar_velocidade()
        angulo = gerar_angulo()
        altura_real = int(calcular_altura_maxima(velocidade, angulo))

        print(f"\n🔢 Tentativa {i + 1} de 3:")
        print(f"Velocidade: {velocidade} m/s | Ângulo: {angulo}°")
        print("💡 DICA: Digite -1 para exibir o gráfico da trajetória, mas a pontuação valerá apenas 50%!")
        chute = int(input("Qual a sua estimativa para a altura máxima (em metros)? "))

        if chute == -1:
            plotar_trajetoria(velocidade, angulo)
            pontoMaximo = pontoMaximo / 2
            chute = int(input("Qual a sua estimativa para a altura máxima (em metros)? "))

        if chute == altura_real:
            print("✅ Parabéns! Você acertou!")
        else:
            print(f"❌ Errou! A altura correta era: {altura_real} m.")
        pontos += calcular_pontos(pontoMaximo, chute, altura_real)

    return pontos

def plotar_trajetoria(velocidade, angulo):
    angulo_rad = math.radians(angulo)
    g = 9.8
    t_total = (2 * velocidade * math.sin(angulo_rad)) / g
    tempos = [t / 100 for t in range(int(t_total * 100) + 1)]
    x = [velocidade * math.cos(angulo_rad) * t for t in tempos]
    y = [(velocidade * math.sin(angulo_rad) * t) - (0.5 * g * t**2) for t in tempos]

    plt.plot(x, y)
    plt.title("🌌 Trajetória do Projétil")
    plt.xlabel("Distância (m)")
    plt.ylabel("Altura (m)")
    plt.grid(True)
    plt.show()

# Funções para salvar e carregar pontuações
def pegar_jogadores():
    if not os.path.exists("bd.json"):
        return {}
    with open("bd.json", "r") as bd:
        return json.load(bd)

def salvar_jogadores(jogador):
    jogadores = pegar_jogadores()
    jogadores.update(jogador)
    with open("bd.json", "w") as bd:
        json.dump(jogadores, bd)

def exibir_top_5():
    jogadores = pegar_jogadores()
    top_5 = sorted(jogadores.items(), key=lambda x: x[1], reverse=True)[:5]

    print("\n🏆 TOP 5 JOGADORES 🏆")
    for i, (nome, pontos) in enumerate(top_5, start=1):
        print(f"{i}º Lugar: {nome} - {pontos} pontos")
    print()

# Programa principal
def main():
    nome = boas_vindas()
    pontos = 0

    opcao = menu()

    if opcao == 1:
        pontos = adivinha_distancia()
    elif opcao == 2:
        pontos = adivinha_altura()

    print("\nObrigado por jogar! 🎮")
    print(f"Sua pontuação final: {pontos} pontos.")
    salvar_jogadores({nome: pontos})
    exibir_top_5()

if __name__ == "__main__":
    main()
