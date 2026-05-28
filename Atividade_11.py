from pygame import *
import sys 

init()
screen = display.set_mode((1280, 720))
display.set_caption("My Lord")

clock = time.Clock()

# --- CARREGAMENTO DAS IMAGENS (SUAS SPRITESHEETS) ---
boy_fight = image.load("Atividade_11/pixelArt/fighter/Attack_01.png")
samurai_walk = image.load("Atividade_11/pixelArt/samurai/walk.png")
shinobi_jump = image.load("Atividade_11/pixelArt/shinobi/Jump.png")

# --- 1. VARIÁVEIS DO FIGHTER (APENAS ATACA) ---
boy_x, boy_y = 100, 300
curr_frame_b = 0
anim_time_b = 0

# --- 2. VARIÁVEIS DO SAMURAI (ANDA APENAS COM 'L') ---
samurai_x, samurai_y = 100, 100
curr_frame_s = 0
anim_time_s = 0
vel_samurai_x = 4
samurai_olhando_direita = True
# --- 3. VARIÁVEIS DO SHINOBI (CONTROLE COMPLETO: ANDA E PULA) ---
shinobi_x, shinobi_y = 100, 500
CHAO_SHINOBI_Y = 500  # Altura padrão do chão para ele

vel_shinobi_x = 0
vel_shinobi_y = 0
VEL_MOV_SHINOBI = 6
FORCA_PULO_SHINOBI = -16
GRAVIDADE = 0.7

esta_no_chao_shinobi = True
shinobi_olhando_direita = True
shinobi_andando = False

curr_frame_n = 0
anim_time_n = 0

# --- LOOP PRINCIPAL ---
while True:
    # Eventos do Sistema
    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit()

    # Captura do teclado para os estados continuos
    teclas = key.get_pressed()
    dt = clock.get_time()

    # =========================================================================
    # LÓGICA 1: FIGHTER (Ataque Contínuo)
    # =========================================================================
    anim_time_b += dt
    if anim_time_b / 1000 > 0.15:  # Velocidade do ataque
        curr_frame_b += 1
        if curr_frame_b > 3:  # Ajuste baseado no tamanho da sua animação (4 frames)
            curr_frame_b = 0
        anim_time_b = 0

    # =========================================================================
    # LÓGICA 2: SAMURAI (Movimentação e Direção )
    # =========================================================================
    velocidade_atual_samurai = 0  # Zera a velocidade a cada frame
    samurai_andando = False
    
    if teclas[K_l]:  # Direita
        velocidade_atual_samurai = vel_samurai_x
        samurai_olhando_direita = True
        samurai_andando = True
    elif teclas[K_k]:  # Esquerda
        velocidade_atual_samurai = -vel_samurai_x
        samurai_olhando_direita = False
        samurai_andando = True

    # Atualiza a posição X do samurai usando a velocidade 
    samurai_x += velocidade_atual_samurai

    # Controle da animação baseado no movimento
    if samurai_andando:
        anim_time_s += dt
        if anim_time_s / 1000 > 0.1:
            curr_frame_s += 1
            if curr_frame_s > 7:  # Loop dos 8 frames de corrida
                curr_frame_s = 0
            anim_time_s = 0
    else:
        curr_frame_s = 0  # Frame parado se soltar as teclas


    # =========================================================================
    # LÓGICA 3: SHINOBI (Movimentação com setas/AWSD e Pulo com Espaço)
    # =========================================================================
    vel_shinobi_x = 0
    shinobi_andando = False

    # Controles laterais (A/D ou Setas)
    if teclas[K_a] :
        vel_shinobi_x = -VEL_MOV_SHINOBI
        shinobi_olhando_direita = False
        shinobi_andando = True
    if teclas[K_d] :
        vel_shinobi_x = VEL_MOV_SHINOBI
        shinobi_olhando_direita = True
        shinobi_andando = True

    # Comando de pulo
    if teclas[K_w] and esta_no_chao_shinobi:
        vel_shinobi_y = FORCA_PULO_SHINOBI
        esta_no_chao_shinobi = False

    # Física de gravidade aplicada ao Shinobi
    vel_shinobi_y += GRAVIDADE
    shinobi_x += vel_shinobi_x
    shinobi_y += vel_shinobi_y

    # Limitador do chão para o Shinobi
    if shinobi_y >= CHAO_SHINOBI_Y:
        shinobi_y = CHAO_SHINOBI_Y
        vel_shinobi_y = 0
        esta_no_chao_shinobi = True

    # Animação do Shinobi baseada no estado (se pular usa a folha de pulo)
    anim_time_n += dt
    if not esta_no_chao_shinobi:
        # Se estiver no ar, avança os quadros do pulo
        if anim_time_n / 1000 > 0.08:
            curr_frame_n += 1
            if curr_frame_n > 11:  # Mantém no último quadro se ainda estiver caindo
                curr_frame_n = 11
            anim_time_n = 0
    elif shinobi_andando:
        # Se estiver no chão andando (como você usa a mesma sprite para teste, ele vai animar o corte)
        if anim_time_n / 1000 > 0.1:
            curr_frame_n += 1
            if curr_frame_n > 11:
                curr_frame_n = 0
            anim_time_n = 0
    else:
        curr_frame_n = 0  # Parado no chão

    # =========================================================================
    # RENDERIZAÇÃO (DESENHO NA TELA)
    # =========================================================================
    screen.fill((255, 255, 255))  # Limpa a tela com fundo branco

    # 1. Desenha o Fighter (Ataque contínuo)
    screen.blit(boy_fight, (boy_x, boy_y), (128 * (curr_frame_b % 4), 128 * (curr_frame_b // 4), 128, 128))

    # 2. Desenha o Samurai (Criando a superfície isolada, invertendo e desenhando)
    samurai_surface = Surface((128, 128), SRCALPHA)
    samurai_surface.blit(samurai_walk, (0, 0), (128 * (curr_frame_s % 8), 128 * (curr_frame_s // 8), 128, 128))
    
    if not samurai_olhando_direita:
        samurai_surface = transform.flip(samurai_surface, True, False)
    
    screen.blit(samurai_surface, (samurai_x, samurai_y))

    # 3. Desenha o Shinobi
    shinobi_surface = Surface((128, 128), SRCALPHA)
    shinobi_surface.blit(shinobi_jump, (0, 0), (128 * (curr_frame_n % 12), 128 * (curr_frame_n // 12), 128, 128))
    
    if not shinobi_olhando_direita:
        shinobi_surface = transform.flip(shinobi_surface, True, False)

    screen.blit(shinobi_surface, (shinobi_x, shinobi_y))

    # Atualização da tela e controle de FPS
    display.update()
    clock.tick(60)
