# Jogo da Forca com Pygame

import pygame
import random

# Inicialização do Pygame
pygame.init()

# Configurações de Cores e Tela
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
LARGURA, ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("JOGO DA FORCA - PYGAME")

# Fontes
FONTE_PALAVRA = pygame.font.SysFont("arial", 40, bold=True)
FONTE_INFO = pygame.font.SysFont("arial", 25)

def reset_jogo():
    # LISTA DE PALAVRAS (Tema: Países) 
    palavras = ["BRASIL", "ARGENTINA", "PORTUGAL", "ALEMANHA", "JAPAO", "FRANCA"]
    palavra = random.choice(palavras).upper()
    return palavra, [], 6

def desenhar(palavra, letras_tentadas, vidas):
    tela.fill(BRANCO)
    
    # Desenho da Forca (Simples)
    pygame.draw.line(tela, PRETO, (100, 500), (300, 500), 5) # Base
    pygame.draw.line(tela, PRETO, (200, 500), (200, 100), 5) # Poste
    pygame.draw.line(tela, PRETO, (200, 100), (400, 100), 5) # Topo
    pygame.draw.line(tela, PRETO, (400, 100), (400, 150), 5) # Corda

    # Boneco baseado nas vidas 
    if vidas <= 5: pygame.draw.circle(tela, PRETO, (400, 190), 40, 5) # Cabeça
    if vidas <= 4: pygame.draw.line(tela, PRETO, (400, 230), (400, 400), 5) # Corpo
    if vidas <= 3: pygame.draw.line(tela, PRETO, (400, 250), (350, 320), 5) # Braço E
    if vidas <= 2: pygame.draw.line(tela, PRETO, (400, 250), (450, 320), 5) # Braço D
    if vidas <= 1: pygame.draw.line(tela, PRETO, (400, 400), (350, 500), 5) # Perna E
    if vidas == 0: pygame.draw.line(tela, PRETO, (400, 400), (450, 500), 5) # Perna D

    # Exibição da Palavra 
    exibicao = ""
    for letra in palavra:
        if letra in letras_tentadas:
            exibicao += letra + " "
        else:
            exibicao += "_ "
    
    texto_palavra = FONTE_PALAVRA.render(exibicao, True, PRETO)
    tela.blit(texto_palavra, (450, 250))

    # Info de Vidas e Letras
    texto_vidas = FONTE_INFO.render(f"Vidas restantes: {vidas}", True, (200, 0, 0))
    tela.blit(texto_vidas, (20, 20))
    
    texto_letras = FONTE_INFO.render(f"Letras: {', '.join(letras_tentadas)}", True, PRETO)
    tela.blit(texto_letras, (20, 550))

    pygame.display.update()

def main():
    palavra, letras_tentadas, vidas = reset_jogo()
    chute_palavra = ""
    rodando = True
    venceu = False

    while rodando:
        desenhar(palavra, letras_tentadas, vidas)

        # Checar vitória/derrota
        venceu = all(letra in letras_tentadas for letra in palavra)
        
        if venceu or vidas == 0:
            pygame.time.delay(1000)
            tela.fill(BRANCO)
            msg = "VOCÊ VENCEU!" if venceu else f"GAME OVER! ERA: {palavra}"
            texto_fim = FONTE_PALAVRA.render(msg, True, PRETO)
            texto_retry = FONTE_INFO.render("Pressione R para Reiniciar ou ESC para Sair", True, PRETO)
            tela.blit(texto_fim, (LARGURA//4, ALTURA//2))
            tela.blit(texto_retry, (LARGURA//4, ALTURA//2 + 60))
            pygame.display.update()

            #  Reiniciar Jogo
            esperando = True
            while esperando:
                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT: return
                    if evento.type == pygame.KEYDOWN:
                        if evento.key == pygame.K_r:
                            palavra, letras_tentadas, vidas = reset_jogo()
                            esperando = False
                        if evento.key == pygame.K_ESCAPE: return

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            if evento.type == pygame.KEYDOWN:
                # Validação: Apenas Letras
                if pygame.K_a <= evento.key <= pygame.K_z:
                    letra = pygame.key.name(evento.key).upper()
                    
                    if letra not in letras_tentadas:
                        letras_tentadas.append(letra)
                        if letra not in palavra:
                            vidas -= 1

    pygame.quit()


main()
