import pygame
import sys
import random
import math

# --- CONFIGURAÇÕES ---
pygame.init()
LARGURA, ALTURA = 800, 600
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Sistema PUC - Casa e Forca")

# Cores
BRANCO, PRETO = (255, 255, 255), (0, 0, 0)
VERDE, VERMELHO = (34, 139, 34), (200, 0, 0)
AZUL_CEU, MARROM = (135, 206, 235), (139, 69, 19)
AMARELO, CINZA = (255, 215, 0), (100, 100, 100)

FONTE = pygame.font.SysFont("Arial", 24)
FONTE_TITULO = pygame.font.SysFont("Arial", 40, bold=True)

# --- LÓGICA DE VALIDAÇÃO (SEU DESAFIO) ---
def validar_email(email): return email.endswith("@puc.com")

def senha_eh_segura(senha):
    if len(senha) < 8: return False
    return any(c.isupper() for c in senha) and any(c.islower() for c in senha) and any(c.isdigit() for c in senha)

def criptografar_cesar(senha):
    res = ""
    inicio, fim = ord('0'), ord('z')
    for c in senha:
        if inicio <= ord(c) <= fim:
            res += chr((ord(c) - inicio + 3) % (fim - inicio + 1) + inicio)
        else: res += c
    return res

# --- FUNÇÕES DE DESENHO ---
def desenhar_casa_tela(nuvem_x, mouse_pos):
    TELA.fill(AZUL_CEU)
    pygame.draw.rect(TELA, VERDE, (0, 500, 800, 100)) # Gramado
    
    # Sol seguindo o mouse
    mx, my = mouse_pos
    pygame.draw.circle(TELA, AMARELO, (mx, my), 40)
    for i in range(0, 360, 45): # Raios do sol
        rad = math.radians(i)
        pygame.draw.line(TELA, AMARELO, (mx + math.cos(rad)*45, my + math.sin(rad)*45), (mx + math.cos(rad)*60, my + math.sin(rad)*60), 3)

    # Nuvens
    for offset in [0, 400]:
        x = (nuvem_x + offset) % LARGURA
        pygame.draw.circle(TELA, BRANCO, (x, 100), 30)
        pygame.draw.circle(TELA, BRANCO, (x + 40, 100), 40)
        pygame.draw.circle(TELA, BRANCO, (x + 80, 100), 30)

    # Casa
    pygame.draw.rect(TELA, (255, 230, 150), (250, 250, 300, 250)) # Parede
    pygame.draw.polygon(TELA, VERMELHO, [(230, 250), (400, 100), (570, 250)]) # Telhado
    pygame.draw.rect(TELA, MARROM, (370, 380, 60, 120)) # Porta
    pygame.draw.rect(TELA, BRANCO, (280, 300, 60, 60)) # Janela

def desenhar_forca(erros):
    pygame.draw.line(TELA, PRETO, (100, 500), (300, 500), 5) # Base
    pygame.draw.line(TELA, PRETO, (200, 500), (200, 150), 5) # Poste
    pygame.draw.line(TELA, PRETO, (200, 150), (350, 150), 5) # Topo
    pygame.draw.line(TELA, PRETO, (350, 150), (350, 200), 5) # Corda
    partes = [
        lambda: pygame.draw.circle(TELA, PRETO, (350, 230), 30, 5), # Cabeça
        lambda: pygame.draw.line(TELA, PRETO, (350, 260), (350, 400), 5), # Corpo
        lambda: pygame.draw.line(TELA, PRETO, (350, 300), (300, 350), 5), # Braço E
        lambda: pygame.draw.line(TELA, PRETO, (350, 300), (400, 350), 5), # Braço D
        lambda: pygame.draw.line(TELA, PRETO, (350, 400), (310, 480), 5), # Perna E
        lambda: pygame.draw.line(TELA, PRETO, (350, 400), (390, 480), 5), # Perna D
    ]
    for i in range(min(erros, len(partes))): partes[i]()

# --- CLASSES DE INTERFACE ---
class Botao:
    def __init__(self, x, y, w, h, texto, cor):
        self.rect = pygame.Rect(x, y, w, h)
        self.texto, self.cor = texto, cor
    def desenhar(self):
        pygame.draw.rect(TELA, self.cor, self.rect, border_radius=10)
        t = FONTE.render(self.texto, True, BRANCO)
        TELA.blit(t, (self.rect.centerx - t.get_width()//2, self.rect.centery - t.get_height()//2))
    def clicou(self, pos): return self.rect.collidepoint(pos)

class InputBox:
    def __init__(self, x, y, w, h, label, segredo=False):
        self.rect = pygame.Rect(x, y, w, h)
        self.text, self.label, self.active, self.segredo = '', label, False, segredo
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN: self.active = self.rect.collidepoint(event.pos)
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE: self.text = self.text[:-1]
            else: self.text += event.unicode
    def draw(self):
        lbl = FONTE.render(self.label, True, PRETO)
        TELA.blit(lbl, (self.rect.x, self.rect.y - 30))
        pygame.draw.rect(TELA, AZUL_CEU if self.active else CINZA, self.rect, 2)
        txt = "*" * len(self.text) if self.segredo else self.text
        TELA.blit(FONTE.render(txt, True, PRETO), (self.rect.x + 5, self.rect.y + 5))

# --- MAIN LOOP ---
def main():
    clock = pygame.time.Clock()
    estado = "LOGIN"
    input_email = InputBox(250, 200, 300, 40, "E-mail (@puc.com):")
    input_senha = InputBox(250, 300, 300, 40, "Senha:", segredo=True)
    msg_erro = ""

    btn_casa = Botao(150, 300, 200, 50, "IR PARA CASA", VERDE)
    btn_forca = Botao(450, 300, 200, 50, "IR PARA FORCA", VERMELHO)

    nuvem_x = 0
    palavra = "PUCPR"; letras = []; erros = 0

    while True:
        TELA.fill(BRANCO)
        m_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            
            if estado == "LOGIN":
                input_email.handle_event(event)
                input_senha.handle_event(event)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    if not validar_email(input_email.text): msg_erro = "E-mail deve ser @puc.com"
                    elif not senha_eh_segura(input_senha.text): msg_erro = "Senha insegura!"
                    else:
                        print(f"🔒 Senha Cripto: {criptografar_cesar(input_senha.text)}")
                        estado = "MENU"; msg_erro = ""
            
            elif estado == "MENU":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if btn_casa.clicou(m_pos): estado = "CASA"
                    if btn_forca.clicou(m_pos): estado = "FORCA"
            
            elif estado == "FORCA":
                if event.type == pygame.KEYDOWN and event.unicode.isalpha():
                    L = event.unicode.upper()
                    if L not in letras:
                        letras.append(L); (erros := erros + 1) if L not in palavra else None

        # --- ATUALIZAÇÃO E DESENHO ---
        if estado == "LOGIN":
            TELA.blit(FONTE_TITULO.render("Acesso Restrito", True, PRETO), (260, 100))
            input_email.draw(); input_senha.draw()
            if msg_erro: TELA.blit(FONTE.render(msg_erro, True, VERMELHO), (250, 400))
        
        elif estado == "MENU":
            TELA.blit(FONTE_TITULO.render("Escolha o seu Destino", True, PRETO), (220, 150))
            btn_casa.desenhar(); btn_forca.desenhar()
        
        elif estado == "CASA":
            # Movimento da Nuvem (Auto + Teclas A/D)
            nuvem_x += 0.5
            keys = pygame.key.get_pressed()
            if keys[pygame.K_d]: nuvem_x += 5
            if keys[pygame.K_a]: nuvem_x -= 5
            desenhar_casa_tela(nuvem_x, m_pos)
            TELA.blit(FONTE.render("ESC para voltar | A/D move nuvens", True, PRETO), (20, 20))
            if keys[pygame.K_ESCAPE]: estado = "MENU"
            
        elif estado == "FORCA":
            desenhar_forca(erros)
            p = " ".join([l if l in letras else "_" for l in palavra])
            TELA.blit(FONTE_TITULO.render(p, True, PRETO), (400, 250))
            TELA.blit(FONTE.render("ESC para sair", True, CINZA), (20, 20))
            if erros >= 6 or all(l in letras for l in palavra):
                txt = "GANHOU!" if erros < 6 else "PERDEU! Palavra: " + palavra
                TELA.blit(FONTE.render(txt, True, VERMELHO), (400, 350))
            if pygame.key.get_pressed()[pygame.K_ESCAPE]: 
                estado = "MENU"; erros = 0; letras = []

        pygame.display.flip()
        clock.tick(60)

main()
