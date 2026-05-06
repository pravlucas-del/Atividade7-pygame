import pygame

pygame.init()
tela = pygame.display.set_mode((400, 300))
fonte = pygame.font.Font(None, 32)

# Variáveis para armazenar o texto
email = ""
senha = ""
campo_ativo = "email"  # Controla qual campo recebe a digitação

executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False
            
        if evento.type == pygame.KEYDOWN:
            # Alternar entre campos com a tecla TAB
            if evento.key == pygame.K_TAB:
                campo_ativo = "senha" if campo_ativo == "email" else "email"
            
            # Lógica de digitação
            elif evento.key == pygame.K_BACKSPACE:
                if campo_ativo == "email": email = email[:-1]
                else: senha = senha[:-1]
            else:
                if campo_ativo == "email": email += evento.unicode
                else: senha += evento.unicode

    tela.fill((30, 30, 30))

    # Renderizar E-mail
    txt_email = fonte.render(f"Email: {email}", True, (255, 255, 255))
    tela.blit(txt_email, (50, 50))

    # Renderizar Senha (usando '*' para esconder os caracteres)
    oculto = "*" * len(senha)
    txt_senha = fonte.render(f"Senha: {oculto}", True, (255, 255, 255))
    tela.blit(txt_senha, (50, 100))

    # Indicador de campo ativo
    cor_foco = (0, 255, 0)
    pos_y = 75 if campo_ativo == "email" else 125
    pygame.draw.rect(tela, cor_foco, (50, pos_y, 200, 2), 2)

    pygame.display.flip()

pygame.quit()
