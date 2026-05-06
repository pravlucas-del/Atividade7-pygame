from random import choice
from unittest import case

from pygame import *
import sys


# variáveis
mensagem_voltar = 'pressione enter para jogar de novo ou backspace para voltar'
jogo = 'login'
erros = 0
tema = ''
palavra = ''
palavra_forca = ''
letras_tentadas = []
final = False
pressionado = False
texto = 'Pressione enter após inserir email e senha'
chute = ''
texto_extra = ''
jogada = 0
adivinha = ''
pontos = 0
ppt_computador = 0
num_aleatorio = 0
num_chute = 0
min = 1
max = 1023
tentativas = 1
segunda_linha = ''
num1 = 0
num2 = 0
resultado = 0
opera = ''
email = ''
senha = ''
cripto = ''
inseriu_email = False
inseriu_senha = False
cloud_x = 800
cloud_direction = 'right'
sun_x = 500
sun_y = 100

# Estado do Jokenpô
opcoes = ["pedra", "papel", "tesoura"]
pontos = 0
resultado_texto = "Escolha sua jogada!"
escolha_comp = ""
escolha_jog = ""

# Listas de palavras para o jogo da forca
palavras_jogos = ['controle', 'console', 'jogo', 'videogame', 'xbox', 'playstation', 'nintendo', 'pc', 'gamer', 'multiplayer']

def valida_email(email):
    return email[-8:] == '@puc.com' # Verifica o email se ele é válido
   
def tem_maiuscula(palavra):
    for letra in palavra:
        if "A" < letra < "Z":
            return True
    return False # Retorna falsa se a função não tiver letra maiuscula

def tem_minuscula(palavra):
    for letra in palavra:
        if "a" < letra < "z":
            return True
    return False # Retorna falsa se a função não tiver letra minuscula

def tem_numero(senha):
    for carac in senha:
        if carac.isnumeric():
            return True
    return False # Retorno falsa a função se não possuir algum número 

def valida_senha(senha):
    tamanho = len(senha) >= 8
    maiuscula = tem_maiuscula(senha)
    minuscula = tem_minuscula(senha)
    numero = tem_numero(senha)
    return tamanho and maiuscula and minuscula and numero

def criptografia(senha):
    senha_cripto = ""
    for carac in senha:
        if carac.isdigit():
            ref = ord('0') # 26
            ascii_carac = ord(carac) # Etapa 1
            pos_alpha = ascii_carac - ref # Etapa 2
            pos_alpha += 3 # Etapa 3
            pos_resto = pos_alpha % 26 # Etapa 4
            letra_ascii = chr(ref + pos_resto) # Etapa 5
            senha_cripto += letra_ascii
        elif 'A'<= carac <= 'Z':
            ref = ord('A') # 65
            ascii_carac = ord(carac) # Etapa 1
            pos_alpha = ascii_carac - ref # Etapa 2
            pos_alpha += 3 # Etapa 3
            pos_resto = pos_alpha % 26 # Etapa 4
            letra_ascii = chr(ref + pos_resto) # Etapa 5
            senha_cripto += letra_ascii
        elif 'a' <= carac <= 'z':
            ref = ord('a') # 65
            ascii_carac = ord(carac) # Etapa 1
            pos_alpha = ascii_carac - ref # Etapa 2
            pos_alpha += 3 # Etapa 3
            pos_resto = pos_alpha % 26 # Etapa 4
            letra_ascii = chr(ref + pos_resto) # Etapa 5
            senha_cripto += letra_ascii
        else:
            senha_cripto += carac
    return senha_cripto

def descriptografia(codificado):
    decodificado = ''
    for c in codificado:
        if c.isdigit() or c.isalpha():
            max = 0
            ref = 0
            if c.isdigit():
                ref = ord('0')
                max = ord('9')
            elif c.islower():
                ref = ord('a')
                max = ord('z')
            elif c.isupper():
                ref = ord('A')
                max = ord('Z')
            decimal = ord(c) # transforma na posição na tabela ascii
            decimal -= ref # subtrai o valor de referência
            decimal -= 3 # adiciona 3
            decimal = decimal % (max - ref + 1) # obtem o resto (do máximo menos a referência + 1)
            decimal += ref # soma o valor de referência
            decodificado += chr(decimal) # adiciona o caracter novo na senha criptografada
        else:
            decodificado += c # repete se for caracter especial
    return decodificado

def desenhar_forca():
   # Forca
    draw.line(window, (0, 0, 0), (175, 600), (225, 600), 4)
    draw.line(window, (0, 0, 0), (200, 600), (200, 300), 4)
    draw.line(window, (0, 0, 0), (200, 300), (300, 300), 4)
    draw.line(window, (0, 0, 0), (300, 300), (300, 350), 4)

    if erros >=1:
        draw.circle(window, (0, 0, 0), (300, 375), 25, 4) # cabeça
    if erros >=2:
        draw.line(window, (0, 0, 0), (300, 400), (300, 500), 4) # tronco
    if erros >=3:
        draw.line(window, (0, 0, 0), (300, 400), (250, 450), 4) # braço esquerdo
    if erros >=4:
        draw.line(window, (0, 0, 0), (300, 400), (350, 450), 4) # braço direito
    if erros >=5:
        draw.line(window, (0, 0, 0), (300, 500), (250, 550), 4) # perna esquerda
    if erros >=6:
        draw.line(window, (0, 0, 0), (300, 500), (350, 550), 4) # perna direita

def verificar_vitoria(jogador, computador): # Função para verificar o resultado do Jokenpô
    if jogador == computador:
        return "Empate!"
    elif (jogador == "pedra" and computador == "tesoura") or \
         (jogador == "tesoura" and computador == "papel") or \
         (jogador == "papel" and computador == "pedra"):
        global pontos
        pontos += 1
        return "Você Venceu!"
    else:
        return "Você Perdeu!"


def botoes(modo):
    if modo == 'menu':
        casa(x, y)
        write_text = fonte.render('jogos!', True, medio_escuro)
        window.blit(write_text, (520, 0))
        draw.rect(window, botao, (10, 510, 300, 200), 0, 20)
        window.blit(forca, (85, 535))
        draw.rect(window, botao, (330, 510, 300, 200), 0, 20)
       
        write_text = fonte_mini.render(f'Criptografada: {criptografia}', True, medio_escuro)
        window.blit(write_text, (900, 450))
        write_text = fonte_mini.render(f'Descriptografada: {descriptografia(criptografia)}', True, medio_escuro)
        window.blit(write_text, (900, 480))

    elif modo == 'forca':
        display.set_caption("Jogo da Forca")    
        write_text = fonte.render('temas!', True, medio_escuro)
        window.blit(write_text, (520, 0))
        draw.rect(window, botao, (60, 100, 560, 280), 0, 20)
        window.blit(jogos, (240, 140))
        draw.rect(window, botao, (660, 100, 560, 280), 0, 20)
        palavra_tema = fonte_mini.render(f'Palavra: {palavra_forca}', True, medio_escuro)
        window.blit(palavra_tema, (700, 140))
    elif modo == 'jokenpo':
        draw.rect(window, botao, (60, 60, 360, 600), 0, 20)
        window.blit(pedra, (90, 210))
        draw.rect(window, botao, (460, 60, 360, 600), 0, 20)
        window.blit(papel, (490, 210))
        draw.rect(window, botao, (860, 60, 360, 600), 0, 20)
        window.blit(tesoura, (890, 210))

    elif modo == 'login':
        draw.rect(window, medio_claro, (340, 210, 600, 300), 0, 20)
        write_text = fonte_mini.render('Login:', True, muito_escuro)
        window.blit(write_text, (380, 240))
        draw.rect(window, muito_claro, (380, 270, 520, 50))
        write_text = fonte_mini.render('Senha:', True, muito_escuro)
        window.blit(write_text, (380, 360))
        draw.rect(window, muito_claro, (380, 390, 520, 50))
        write_text = fonte_mini.render(texto, True, escuro)
        text_rect = write_text.get_rect(center=(640, 480))
        window.blit(write_text, text_rect)

        write_text = fonte_mini.render(email, True, escuro)
        window.blit(write_text, (385, 290))
        write_text = fonte_mini.render(senha, True, escuro)
        window.blit(write_text, (385, 410))



        

def casa(x, y):
    global cloud_x, cloud_direction, sun_x, sun_y
    day = Color(16, 198, 229)
    afternoon = Color(236, 174, 121)
    night = Color(0, 39, 89)
    sea = (64, 127, 204)
    sun = (248, 228, 143)
    moon = (229, 229, 229)
    cloud = (202, 204, 207)
    bg_color = day
    # Update
    dt = clock.get_time()/1000


    # Sun position
    keys = key.get_pressed()

    if mouse.get_focused() == False:
        if keys[K_d] or keys[K_RIGHT]:
            sun_x = sun_x + 100 * dt
        elif keys[K_a] or keys[K_LEFT]:
            sun_x = sun_x - 100 * dt
        if keys[K_w] or keys[K_UP]:
            sun_y = sun_y - 100 * dt
        elif keys[K_s] or keys[K_DOWN]:
            sun_y = sun_y + 100 * dt
    else:
        sun_x, sun_y = x, y

    # Draw stuff
    window.fill(bg_color)   

    # Sun / moon
    # Not letting it out of bounds
    if sun_y < 90:
        sun_y = 90
    if sun_y > 630:
        sun_y = 630
    if sun_x > 1140:
        sun_x = 1140
    if sun_x < 40:
        sun_x = 40
    
    # BG color (based on sun/moon position)
    if sun_y < 300:
        bg_color = day.lerp(afternoon, (sun_y-90)/300)
    else:
        bg_color = afternoon.lerp(night, (sun_y-250)/420)

    if sun_y < 550:
        draw.line(window, sun, (sun_x+50, sun_y-90), (sun_x+50, sun_y+90), 3) # top-bottom
        draw.line(window, sun, (sun_x-40, sun_y), (sun_x+140, sun_y), 3) # left-right
        draw.line(window, sun, (sun_x-5, sun_y-55), (sun_x+105, sun_y+55), 2) # top+left-bottom+right
        draw.line(window, sun, (sun_x-5, sun_y+55), (sun_x+105, sun_y-55), 2) # bottom+left-top+right
        draw.circle(window, sun, (sun_x+50, sun_y), 50) # circle
    else:
        draw.circle(window, moon, (sun_x+50, sun_y), 50)

    # Sea
    draw.rect(window, sea, (0, 500, 1280, 220))
    
    # Cloud
    draw.circle(window, cloud, (cloud_x+50, 150), 50)
    draw.circle(window, cloud, (cloud_x+120, 150), 65)
    draw.circle(window, cloud, (cloud_x+190, 150), 65)
    draw.circle(window, cloud, (cloud_x+260, 150), 50)

    if cloud_direction == 'right':
        cloud_x = cloud_x + 100 * dt
        if cloud_x > 970:
            cloud_direction = 'left'
    elif cloud_direction == 'left':
        cloud_x = cloud_x - 100 * dt
        if cloud_x < 0:
            cloud_direction = 'right'

    # House
    draw.rect(window, (187, 116, 86), (320, 260, 240, 240)) # house
    draw.rect(window, (160, 97, 54), (350, 356, 60, 96)) # window
    draw.rect(window, (160, 97, 54), (450, 340, 80, 160)) # door
    draw.polygon(window, (188, 66, 7), ((300, 260), (440, 140), (580, 260))) # top

# Configurações iniciais do Pygame
init()
window = display.set_mode((1280, 720))
display.set_caption("Menu de Login")
clock = time.Clock()
fonte = font.SysFont('Arial', 50)
# CORES
muito_escuro = Color(41, 0, 33)
escuro = Color(61, 0, 50)
medio_escuro = Color(163, 0, 133)
medio = Color(255, 175, 240)
medio_claro = Color(255, 214, 247)
claro = Color(255, 235, 251)
muito_claro = Color(255, 243, 253)
botao = Color(224, 190, 218)




# Loop principal do programa
while running:
    clock.tick(60)
    x, y = mouse.get_pos()

    for ev in event.get():
        if ev.type == QUIT:
            running = False
        if ev.type == MOUSEBUTTONDOWN:
            if ev.button == 1:
                match jogo:
                    case 'menu':
                        if 10 <= x <= 310 and 510 <= y <= 710:
                            jogo = 'forca'
                    case 'forca':
                        if 60 <= x <= 620 and 100 <= y <= 380:
                            palavra = choice(palavras_jogos)
                        palavra_forca = '_' * len(palavra)
                        letras_tentadas = []
                        erros = 0
                        final = False
                        texto_extra = ''
                    case 'jokenpo':
                        if 60 <= x <= 420 and 60 <= y <= 660:
                            escolha_jog = "pedra"
                        elif 460 <= x <= 820 and 60 <= y <= 660:
                            escolha_jog = "papel"
                        elif 860 <= x <= 1220 and 60 <= y <= 660:
                            escolha_jog = "tesoura"
                        if escolha_jog:
                            escolha_comp = choice(opcoes)
                            resultado_texto = verificar_vitoria(escolha_jog, escolha_comp)
        
        if ev.type == KEYDOWN:
            if jogo == 'forca':
                if final == False:
                    pressionado = False
                    if K_a <= ev.key <= K_z:
                        chute += key.name(ev.key)
                    elif ev.key == K_BACKSPACE:
                        chute = chute[:-1]
                    elif ev.key == K_RETURN:
                        pressionado = True
                elif final == True:
                    if ev.key == K_BACKSPACE:
                        jogo = 'menu'
                        texto = ''
                    erros = 0
                    tema = ''
                    palavra = ''
                    final = False
                    pressionado = False
                    chute = ''
                    texto_extra = ''
                    texto = ''
                elif jogo == 'jokenpo':
                    if ev.key == K_BACKSPACE:
                        jogo = 'menu'
                        pontos = 0
                        texto = ''
                    jogada = 0
            else:
                
                if ev.unicode.isdigit():
                    chute += ev.unicode
                    pressionado = False
                elif ev.key == K_BACKSPACE:
                    chute = chute[:-1]
                    pressionado = False
                elif ev.key == K_RETURN:
                    pressionado = True
                    num_chute = int(chute)
                    chute = ''
                if num_chute == num_aleatorio:
                        final = True
            elif jogo == 'login':
                if inseriu_email == False:
                    if ev.key == K_BACKSPACE:
                        email = email[:-1]
                    elif ev.key == K_RETURN:
                            inseriu_email = True
                    else:
                        email += ev.unicode
                elif inseriu_senha == False:
                    if ev.key == K_BACKSPACE:
                        senha = senha[:-1]
                    elif ev.key == K_RETURN:
                            inseriu_senha = True
                            if valida_email(email) and valida_senha(senha):
                                jogo = 'menu'
                                texto = ''
                                cripto = criptografia(senha)
                            else:
                                texto = 'Email ou senha inválido(s).'
                                inseriu_email = False
                                email = ''
                                inseriu_senha = False
                                senha = ''
                    else:
                        senha += ev.unicode

    match jogo:
        case 'forca':
            if tema == '':
                botoes('forca')
            else:
                match tema:
                    case 'jogos':
                        write_text = fonte_menor.render('tema: jogos!', True, medio_escuro)
                        window.blit(write_text, (480, 0))
                        

                desenhar_forca(erros)

                write_text = fonte_menor.render(palavra_forca, True, medio)
                window.blit(write_text, (350, 500))

                write_text = fonte_menor_ainda.render(chute, True, medio)
                window.blit(write_text, (350, 450))
                
                if pressionado:
                    if chute == palavra:
                        final = True
                        texto_extra = ''
                    else:
                        if len(chute) > 1:
                            pressionado = False
                            texto_extra = 'A palavra que você inseriu não está certa!'
                            chute = ''


                texto = 'Letras erradas: '
                segunda_linha = ', '.join(letras_tentadas)

                if pressionado:
                    texto_extra = ''
                    if final == False:
                        if erros < 6:
                            palavra_vazia = ''
                            if chute not in palavra:
                                if chute not in letras_tentadas:
                                    letras_tentadas.append(chute)
                                    erros += 1
                            for i in range(len(palavra)):
                                if chute == palavra[i]:
                                    palavra_vazia += chute
                                else:
                                    palavra_vazia += palavra_forca[i]
                            palavra_forca = palavra_vazia
                            if palavra_forca == palavra:
                                final = True
                        else:
                            final = True
                    else:
                        if erros == 6:
                            texto = 'Que pena, você perdeu! A palavra era:'
                            segunda_linha = palavra
                            texto_extra = mensagem_voltar
                        else:
                            texto = 'Parabéns! Você venceu! A palavra era:'
                            segunda_linha = palavra
                            texto_extra = mensagem_voltar
                            palavra_forca = palavra
                    chute = ''
                
                write_text = fonte_menor_ainda.render(texto, True, medio)
                window.blit(write_text, (370, 250))
                write_text = fonte_menor_ainda.render(segunda_linha, True, medio)
                window.blit(write_text, (370, 320))
                write_text = fonte_mini.render(texto_extra, True, medio)
                window.blit(write_text, (370, 390))
        case 'jokenpo':
            botoes('jokenpo')
            write_text = fonte_menor.render(resultado_texto, True, medio)
            window.blit(write_text, (480, 0))
            if escolha_jog:
                write_text = fonte_menor_ainda.render(f'Você escolheu: {escolha_jog}', True, medio)
                window.blit(write_text, (480, 60))
                write_text = fonte_menor_ainda.render(f'O computador escolheu: {escolha_comp}', True, medio)
                window.blit(write_text, (480, 120))
                write_text = fonte_menor_ainda.render(f'Pontos: {pontos}', True, medio)
                window.blit(write_text, (480, 180))
        case 'menu':
            casa(x, y)
            botoes('menu')
        case 'login':
            botoes('login')



   
    
    
    

    
    
    
    display.update()





