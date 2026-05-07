import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Configurações da tela
LARGURA, ALTURA = 1280, 720
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Login")

# Cores e Fontes
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
CINZA = (200, 200, 200)
fonte = pygame.font.Font(None, 32)

# Variáveis de entrada
usuario = ""
senha = ""
ativo = "usuario" # Define qual campo está ativo
mensagem = ""

# Retângulos para os campos de entrada
rect_usuario = pygame.Rect(100, 100, 200, 32)
rect_senha = pygame.Rect(100, 160, 200, 32)
rect_botao = pygame.Rect(150, 220, 100, 40)

def desenhar_tela():
    tela.fill(BRANCO)
    
    # Desenhar campos e texto
    cor_u = PRETO if ativo == "usuario" else CINZA
    cor_s = PRETO if ativo == "senha" else CINZA
    
    pygame.draw.rect(tela, cor_u, rect_usuario, 2)
    pygame.draw.rect(tela, cor_s, rect_senha, 2)
    pygame.draw.rect(tela, PRETO, rect_botao)
    
    txt_u = fonte.render(usuario, True, PRETO)
    txt_s = fonte.render("*" * len(senha), True, PRETO)
    txt_botao = fonte.render("Entrar", True, BRANCO)
    
    tela.blit(txt_u, (rect_usuario.x + 5, rect_usuario.y + 5))
    tela.blit(txt_s, (rect_senha.x + 5, rect_senha.y + 5))
    tela.blit(txt_botao, (rect_botao.x + 10, rect_botao.y + 10))
    
    # Mensagem de feedback
    txt_msg = fonte.render(mensagem, True, PRETO)
    tela.blit(txt_msg, (50, 50))
    
    pygame.display.flip()

# Loop principal
rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if rect_usuario.collidepoint(event.pos):
                ativo = "usuario"
            elif rect_senha.collidepoint(event.pos):
                ativo = "senha"
            elif rect_botao.collidepoint(event.pos):
                if usuario == "admin" and senha == "1234":
                    mensagem = "Login Sucesso!"
                else:
                    mensagem = "Erro de Login!"

        if event.type == pygame.KEYDOWN:
            if ativo == "usuario":
                if event.key == pygame.K_BACKSPACE:
                    usuario = usuario[:-1]
                else:
                    usuario += event.unicode
            elif ativo == "senha":
                if event.key == pygame.K_BACKSPACE:
                    senha = senha[:-1]
                else:
                    senha += event.unicode

    desenhar_tela()

pygame.quit()
sys.exit()
