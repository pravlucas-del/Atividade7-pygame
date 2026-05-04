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
    



