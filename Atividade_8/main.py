from pygame import *
import sys

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


## Configurar e utilizar o pygame
init()
screen = display.set_mode((1280, 720))
running = True

input_string = ""
valid_email = False
pressed_enter = False
fonte = font.Font(size=50)
fonte_validation = font.Font(size=25)

while running:
    for ev in event.get():
        if ev.type == QUIT:
            running = False
        if ev.type == KEYDOWN:
            if ev.key == K_BACKSPACE:
                input_string = input_string[:-1]
            elif ev.key == K_RETURN:
                pressed_enter = True
                valid_email = valida_email(input_string)
            else:
                input_string += ev.unicode

    screen.fill("white")
    draw.rect(screen, "black", (100, 100, 500, 50), 3)
    input_text = fonte.render(input_string, True, "#000000")
    screen.blit(input_text, (120, 105))
    if pressed_enter:
        if valid_email:
            valid_text = fonte_validation.render("Parabéns, o seu e-mail é válido!", True, "green")
            screen.blit(valid_text, (120, 180))
        else:
            valid_text = fonte_validation.render("O seu e-mail não é válido. Digite novamente!", True, "red")
            screen.blit(valid_text, (120, 180))

    display.update()






