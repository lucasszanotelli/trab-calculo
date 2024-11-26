import json
from random import randint
import math
import matplotlib.pyplot as plt
from time import sleep
import os
from datetime import datetime, timedelta
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

    plt.plot(x, y)
    plt.title("Trajetória do Projétil")
    plt.xlabel("Distância (m)")
    plt.ylabel("Altura (m)")
    plt.grid(True)
    plt.show()

# Programa principal

def boasVindas():
    os.system("cls")
    print("Bem-vindo ao JOJULO")
    # sleep(3)
    os.system("cls")
    print("Você terá 1 minuto para acertar o maior número de cálculos possíveis")
    # sleep(6)
    os.system("cls")
    nome = obterNome()
    # sleep(1)
    os.system("cls")
    print("Olá %s, vamos começar o seu jogo"% nome)
    # sleep(3)
    os.system("cls")
    print("Primeiro, selecione o modo de jogo:")
    return nome

def obterNome():
    nome = str(input("Incialmente, infome o seu nome: "))
    while len(nome)<3:
        print("Nome inválido")
        nome = str(input("Infome o seu nome: "))
    return nome


def iniciarContador():
    print("Você terá 3 tentativas para obter o maior número de pontos")
    sleep(3)
    for i in range(3, 0, -1):
        print("O jogo começa em %d.."%i)
        sleep(1)

def tem_tempo(start: datetime) -> bool:
    return start + timedelta(minutes=1) > datetime.now()

def adivinhaDistancia():
    pontos = 0
    iniciarContador()

    for i in range(3):
        velocidade = gerar_velocidade()
        angulo = gerar_angulo()
        distancia_real = int(calcular_distancia(velocidade, angulo))
        
        print("\nAdivinhe a Distância - VALOR INTEIRO")
        print("Velocidade: %.2f" %velocidade)
        print("Ângulo: %d°\n" %angulo)

        chute = int(input("Informe sua estimativa para a distância (em metros): "))
        if (chute == distancia_real): print("VOCÊ ACERTOU!")
        else: print("ERROU! Valor correto: %d" %distancia_real)
        
        x = calcularPontos(chute,distancia_real)
        pontos+=x

    return pontos

def calcularPontos(chute, valorReal):
    x=(100 - abs((chute-valorReal)))
    if x<0: x = 0
    print("VOCÊ GANHOU: %d PONTOS!" %x)
    return x


def adivinhaAltura():
    pontos = 0
    iniciarContador()

    for i in range(3):
        velocidade = gerar_velocidade()
        angulo = gerar_angulo()
        altura_real = int(calcular_altura_maxima(velocidade, angulo))

        chute = int(input("Informe sua estimativa para a altura máxima (em metros): "))
        
        print("\nAdivinhe a Distância - VALOR INTEIRO")
        print("Velocidade: %.2f" %velocidade)
        print("Ângulo: %d°\n" %angulo)

        chute = int(input("Informe sua estimativa para a distância (em metros): "))
        if (chute == altura_real): print("VOCÊ ACERTOU!")
        else: print("ERROU! Valor correto: %d" %altura_real)
        
        x = calcularPontos(chute,altura_real)
        pontos+=x

    return pontos

def main():
    
    nome = boasVindas()
    opcao = menu()

    if opcao == 0:
            print("\nFim do jogo! Pontuação final:", pontos)
            return
    elif opcao == 1:
        pontos = adivinhaDistancia()
    elif opcao == 2:
        pontos = adivinhaAltura()

    print("VOCÊ GANHOU %d PONTOS!" %pontos)
    print("OBRIGADO POR JOGAR, %s!" %nome.upper())

    salvar_jogadores({nome: pontos,})

    for nome, pontos in pegar_jogadores().items():
        print(nome, pontos)



    # elif opcao == 3:
    #     print("\nPlotando a trajetória do projétil...")
    #     plotar_trajetoria(velocidade, angulo)
    # input("Pressione Enter para continuar...")




def pegar_jogadores() -> dict[str, int]:
    with open('bd.json', 'r') as bd:
        return json.loads(bd.read())
    
def salvar_jogadores(jogador: dict[str, int]):
    jogadores = pegar_jogadores()

    with open('bd.json', 'w') as bd:
        bd.write(json.dumps(jogadores | jogador))



main()
