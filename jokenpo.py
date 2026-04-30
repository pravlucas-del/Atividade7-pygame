import pygame
import random
import sys

# Inicialização
pygame.init()
LARGURA, ALTURA = 600, 400
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jokenpô - Pedra, Papel, Tesoura")

# Cores e Fontes
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
CINZA = (200, 200, 200)
fonte = pygame.font.SysFont("Arial", 32)
fonte_pequena = pygame.font.SysFont("Arial", 24)

# Estado do Jogo
opcoes = ["pedra", "papel", "tesoura"]
pontos = 0
resultado_texto = "Escolha sua jogada!"
escolha_comp = ""
escolha_jog = ""

def verificar_vitoria(jogador, computador):
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

# Loop Principal
executando = True
while executando:
    tela.fill(BRANCO)
    
    # Desenhar Botões (Retângulos)
    btn_pedra = pygame.draw.rect(tela, CINZA, (50, 250, 120, 50))
    btn_papel = pygame.draw.rect(tela, CINZA, (240, 250, 120, 50))
    btn_tesoura = pygame.draw.rect(tela, CINZA, (430, 250, 120, 50))
    
    # Textos dos Botões
    tela.blit(fonte_pequena.render("Pedra", True, PRETO), (75, 260))
    tela.blit(fonte_pequena.render("Papel", True, PRETO), (270, 260))
    tela.blit(fonte_pequena.render("Tesoura", True, PRETO), (450, 260))
    
    # Exibir Pontuação e Resultados
    tela.blit(fonte.render(f"Pontos: {pontos}", True, PRETO), (20, 20))
    tela.blit(fonte.render(resultado_texto, True, PRETO), (180, 100))
    if escolha_comp:
        tela.blit(fonte_pequena.render(f"PC escolheu: {escolha_comp}", True, PRETO), (210, 160))

    # Botão Reiniciar
    btn_reset = pygame.draw.rect(tela, (255, 100, 100), (240, 330, 120, 40))
    tela.blit(fonte_pequena.render("Resetar", True, BRANCO), (265, 335))

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False
        
        if evento.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            
            # Lógica das Escolhas
            jogada = ""
            if btn_pedra.collidepoint(pos): jogada = "pedra"
            elif btn_papel.collidepoint(pos): jogada = "papel"
            elif btn_tesoura.collidepoint(pos): jogada = "tesoura"
            
            if jogada:
                escolha_jog = jogada
                escolha_comp = random.choice(opcoes) # Computador gera resultado
                resultado_texto = verificar_vitoria(escolha_jog, escolha_comp) # Condição de vitória
            
            # Reiniciar o jogo
            if btn_reset.collidepoint(pos):
                pontos = 0
                resultado_texto = "Escolha sua jogada!"
                escolha_comp = ""

    pygame.display.flip()

pygame.quit()
sys.exit()
