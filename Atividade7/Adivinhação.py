# Jogo da Adivinhação

import random

def jogo_adivinhacao():
    print("--- JOGO DE ADIVINHAÇÃO (1-1023) ---")
    modo = input("Quem vai adivinhar? (1-Usuário / 2-Computador): ")

    alvo = random.randint(1, 1023)
    tentativas = 0

    if modo == '1':
        while True:
            tentativas += 1
            chute = int(input(f"Tentativa {tentativas} - Seu palpite: "))
            
            if alvo < chute:
                print("-1")
            elif alvo > chute:
                print("1")
            else:
                print(f"0\nParabéns! Você acertou em {tentativas} tentativas.")
                
    else:
        print("Pense em um número de 1 a 1023 e não conte para mim!")
        inicio, fim = 1, 1023
        
        while True:
            tentativas += 1
            chute = (inicio + fim) // 2
            print(f"O computador chutou: {chute}")
            
            # O usuário fornece o feedback baseado na lógica pedida
            feedback = int(input("Feedback (-1: Menor, 1: Maior, 0: Acertou): "))
            
            if feedback == -1:
                fim = chute - 1
            elif feedback == 1:
                inicio = chute + 1
            elif feedback == 0:
                print(f"O computador venceu com {tentativas} tentativas!")
                break
                

jogo_adivinhacao()
