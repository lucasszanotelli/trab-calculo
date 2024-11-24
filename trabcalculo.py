#CALCULAR A ALTURA MÁXIMA DE UM PROJÉTIL SABENDO A VELOCIDADE INICIAL (aleatório)  E O ÂNGULO ( 30,45,60 ) -> aleatorio
#CALCULAR A DISTÂNCIA PERCORRIDA PELO PROJÉTIL
#INSERIR UM JOGO PARA QUE O USUÁRIO INFORME UM POSSÍVEL VALOR DE DISTÂNCIA
#SE ACERTAR, GANHA PONTO
#PLOTAR O GRÁFICO

from random import randint
import math
#import matplotlib.pyplot as plt

#VALOR RANDOMICO DO ANGULO E DA VELOCIDADE
def gerar_angulo():
    vetor = [30, 45, 60]
    indice = randint(0,2)
    return (vetor[indice]) 

def gerar_velocidade():
    velocidade = randint(1,100)
    return velocidade

#FUNÇÃO PARA CALCULAR A DISTANCIA
def distancia():
    velocidade = gerar_velocidade()
    angulo_aleatorio = gerar_angulo()
    angulo = math.radians(angulo_aleatorio)

    #mostrando na tela para possivel conferencia
    print("DADOS")
    print(f'velocidade: {velocidade}')
    print(f'angulo em graus: {angulo_aleatorio}°')

    altura_maxima = (pow(velocidade , 2) * pow(math.sin(angulo), 2)) / (2 * 9.8)
    return altura_maxima

def menu():
    op = ""
    while op.isdigit() == False or int(op) < 0 or int(op) > 6:

        print("\n")        
        print("JOGO")
        print("1 - Distância")
        print("2 - Altura Máxima")
        print("3 - Plotar")
        print("0-Sair")
        op = input("Escolha sua opção: ")
    return int(op)

################ PROGRAMA PRINCIPAL ####################
d = distancia()

pontos = 0

op = 1
while op != 0:
        op = menu()
        
        if op == 0:
            print("\n\nFim do programa!!!\n\n")
            
        elif op == 1:
            print("\n\nDISTÂNCIA\n\n")    
            possibilidade = int(input("Informe a possível distância: "))
            if possibilidade>d:
                calculo = possibilidade - d
            elif d>possibilidade:
                calculo = d -possibilidade
            else:
                print("Parabéns! Você acertou!")
                pontos = 10

            if calculo > 0 and calculo < 1:
                pontos += 5
            elif calculo >2:
                pontos += 2
            else:
                pontos += 1

         
        elif op == 2:
            print("\n\nALTURA MÁXIMA\n\n")
 


        elif op == 3:
            print("\n\nPLOTAR GRÁFICO\n\n")
            # Ler a informação para pesquisar


        else:
            print("Opção inválida!")

        input("Pressione <enter> para continuar ...")
    



