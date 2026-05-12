from turtle import *
from random import randint
from time import sleep


t = Turtle()
t.speed(0)
colormode(255)
sleep 
#t.screen.bgcolor('black')


def randomColor():
    r = randint(0,255) # Gera um valor aleatório para a componente vermelha (R) da cor
    g = randint(0,255) # Gera um valor aleatório para a componente verde (G) da cor
    b = randint(0,255) # Gera um valor aleatório para a componente azul (B) da cor
    return (r, g, b) # Aleatório entre 0 e 255 para cada componente de cor (R, G, B)

def drawSquare(t,size):
    t.pu() # Levanta a caneta para não desenhar enquanto se move para a posição inicial
    t.pd() # Levanta a caneta para não desenhar enquanto se move para a posição inicial
    #t.color(randomColor())
    t.begin_fill() # Inicia o preenchimento do quadrado
    t.fillcolor(randomColor()) # Define a cor de preenchimento usando a função randomColor()
    for _ in range(4): # Desenha um quadrado
        t.fd(size) # Move para frente com o tamanho especificado
        t.rt(90) # Gira 90 graus para a direita
    t.end_fill() # Finaliza o preenchimento do quadrado

def drawSquareFractal(t,size,step = 50):
    if size == 0: # Condição de parada para a recursão, quando o tamanho do quadrado for 0, a função retorna sem fazer nada
        return
    t.goto(100,-10) # Move a tartaruga para a posição (0, 0) para centralizar o desenho
    t.fd(size / 1.5) # Move para frente com um deslocamento proporcional ao tamanho do quadrado atual
    t.lt(10) # Gira 10 graus para a esquerda para criar um efeito de rotação no fractal
    drawSquare(t,size) # Chama a função drawSquare para desenhar um quadrado com o tamanho atual
    drawSquareFractal(t,size-1,step) # Chama a função drawSquareFractal recursivamente com um tamanho reduzido para criar o efeito de fractal
    #t.clear() # Limpa a tela para desenhar o próximo quadrado do fractal
  
def estrela(t,size):
    if size == 0: # Condição de parada para a recursão, quando o tamanho da estrela for 0, a função retorna sem fazer nada
        return
    t.color(randomColor()) # Define a cor da caneta usando a função randomColor()
    t.fd(size) # Move para frente com o tamanho especificado
    t.rt(144) # Gira 144 graus para a direita para criar a forma de estrela
    estrela(t,size-10) # Chama a função estrela recursivamente com um tamanho reduzido para criar o efeito de fractal

def arvore(t,size):
    if size == 0: # Condição de parada para a recursão, quando o tamanho do ramo for 0, a função retorna sem fazer nada
        return
    t.color(randomColor()) # Define a cor da caneta usando a função randomColor()
    t.fd(size) # Move para frente com o tamanho especificado
    t.lt(30) # Gira 30 graus para a esquerda para criar o efeito de ramificação
    arvore(t,size-10) # Chama a função arvore recursivamente com um tamanho reduzido para criar o próximo ramo da árvore
    t.rt(60) # Gira 60 graus para a direita para criar o efeito de ramificação
    arvore(t,size-10) # Chama a função arvore recursivamente com um tamanho reduzido para criar o próximo ramo da árvore
    t.lt(30) # Gira 30 graus para a esquerda para retornar à posição original
    t.bk(size) # Move para trás com o tamanho especificado para retornar à posição original
    

t.screen.bgcolor("#00567E")
drawSquareFractal(t,200)
sleep(5)
t.clear()
t.screen.bgcolor("#2E0404")
estrela(t,450)
sleep(5)
t.clear()
t.screen.bgcolor("#080852")
t.pu()
t.goto(0,-50)
t.pd()
t.setheading(90)
arvore(t,100)
sleep(5)


mainloop()

drawSquareFractal(t,50)
    



mainloop()
