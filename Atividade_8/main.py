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




