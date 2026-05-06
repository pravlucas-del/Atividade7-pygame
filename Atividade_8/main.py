# from pygame import *
# import sys

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

print(criptografia("ZaNT9PJR"))

#- Implemente um programa no pygame que utilize essas funções na hora de fazer o login, 
# e após os dados serem validados a última versão da casinha deve ser aberta (400XP);
# Configurações iniciais do Pygame
init()
window = display.set_mode((1280, 720))
display.set_caption("Menu de Login")
# Variáveis para armazenar o email e senha
email = ""
senha = ""

# CORES
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)




# Loop principal do programa
while True:
    for e in event.get():
        if e.type == QUIT:
            quit()
            sys.exit()
        if ev.type == MOUSEBUTTONDOWN:
            if ev.button == 1:
                if sun_y < 300:
                    sfx_morning.play()
                elif sun_y < 550:
                    sfx_afternoon.play()
                else:
                    sfx_night.play()
    # Desenhar a tela de login
    window.fill(WHITE)
    # Aqui você pode adicionar os campos de entrada para email e senha, e um botão de login
    # Exemplo de texto para o campo de email e senha
    font = font.SysFont(None, 36)
    email_text = font.render("Email: " + email, True, BLACK)
    senha_text = font.render("Senha: " + senha, True, BLACK)
    window.blit(email_text, (50, 50))
    window.blit(senha_text, (50, 100))
    
    # Ao concluir o login acessar a última versão da casinha (400XP)
    draw.rect(window, BLUE, (50, 150, 200, 100)) # Exemplo de um botão de login
    draw.rect(window, BLACK, (50, 150, 200, 100), 2) # Borda do botão
    button_text = font.render("Login", True, BLACK)
    window.blit(button_text, (90, 180))
    # Verificar se o botão de login foi clicado e validar os dados
    mouse_pos = mouse.get_pos()
    mouse_click = mouse.get_pressed()
    if 50 <= mouse_pos[0] <= 250 and 150 <= mouse_pos[1] <= 250:
        if mouse_click[0]: # Verificar se o botão esquerdo do mouse foi clicado
            if valida_email(email) and valida_senha(senha):
                # Acessar a última versão da casinha (400XP)
                window.fill(WHITE) # Limpar a tela
    
   
    
    # Código da casa
    draw.rect(window, (187, 116, 86), (320, 360, 240, 240)) # casa
    draw.rect(window, (160, 97, 54), (350, 456, 60, 96)) # janela
    draw.rect(window, (160, 97, 54), (450, 440, 80, 160)) # porta
    draw.polygon(window, (188, 66, 7), ((300, 360), (440, 240), (580, 360))) # telhado        
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
        sun_x, sun_y = mouse.get_pos()

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
        text = 'Manhã no mundo de Fairy Tail'
    else:
        bg_color = afternoon.lerp(night, (sun_y-250)/420)
        if sun_y < 550:
            text = 'Tarde no mundo de Fairy Tail'
        else:
            text = 'Noite no mundo de Fairy Tail'

    if sun_y < 550:
        draw.line(window, sun, (sun_x+50, sun_y-90), (sun_x+50, sun_y+90), 3) # cima-baixo
        draw.line(window, sun, (sun_x-40, sun_y), (sun_x+140, sun_y), 3) # esquerda-direita
        draw.line(window, sun, (sun_x-5, sun_y-55), (sun_x+105, sun_y+55), 2) # superior+esquerda-inferior+direita
        draw.line(window, sun, (sun_x-5, sun_y+55), (sun_x+105, sun_y-55), 2) # inferior+esquerda-superior+direita
        draw.circle(window, sun, (sun_x+50, sun_y), 50) # círculo do sol
    else:
        draw.circle(window, moon, (sun_x+50, sun_y), 50)

    # Sea
    draw.rect(window, sea, (0, 600, 1280, 120))
    
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
    

    
    
    
    display.update()






