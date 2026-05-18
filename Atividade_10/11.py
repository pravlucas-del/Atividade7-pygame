import pygame
import random
import sys

# Inicialização do PyGame e da fonte
pygame.init()
pygame.font.init()

# Configurações da Janela
LARGURA, ALTURA = 1000, 700
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Trabalho Prático - Três Histogramas")

# Cores
COR_FUNDO = (20, 20, 20)
COR_EIXO = (240, 240, 240)
COR_TEXTO = (255, 255, 255)
COR_BOTAO = (50, 120, 200)
COR_BOTAO_HOVER = (70, 150, 230)
COR_CAIXA_TEXTO = (40, 40, 40)

# Fontes
fonte_p = pygame.font.SysFont("Arial", 14)
fonte_m = pygame.font.SysFont("Arial", 20, bold=True)
fonte_g = pygame.font.SysFont("Arial", 28, bold=True)

# -------------------------------------------------------------------------
# GERAÇÃO DOS DADOS DOS HISTOGRAMAS
# -------------------------------------------------------------------------

# HISTOGRAMA 1: Lista aleatória com pelo menos 50 números
# Sorteia uma quantidade de itens entre 50 e 80, e valores de 0 a 100
qtd_h1 = random.randint(50, 80)
dados_h1 = [random.randint(0, 100) for _ in range(qtd_h1)]
faixas_h1 = 5  # Diferente para cada histograma

# HISTOGRAMA 2: Lista estática com total de números por faixa aleatório
# Base estática simulada: o valor máximo possível de um elemento é 100
limite_total_h2 = 120 
faixas_h2 = 8  # Diferente para cada histograma
dados_h2 = []

# Distribui uma quantidade aleatória de elementos por faixa sem estourar o limite total
contagem_restante = limite_total_h2
for i in range(faixas_h2):
    tamanho_faixa = 100 // faixas_h2
    min_f = i * tamanho_faixa
    max_f = (i + 1) * tamanho_faixa
    
    # Sorteia quantos números esta faixa vai ter
    qtd_na_faixa = random.randint(0, min(contagem_restante, 20))
    contagem_restante -= qtd_na_faixa
    
    # Adiciona os números estáticos daquela faixa na lista principal
    for _ in range(qtd_na_faixa):
        dados_h2.append(random.randint(min_f, max_f - 1))

# HISTOGRAMA 3: Inicialmente vazio (será preenchido via input do PyGame)
dados_h3 = []
faixas_h3 = 6  # Diferente para cada histograma
input_usuario_texto = ""  # Armazena a string que o usuário digita

# -------------------------------------------------------------------------
# FUNÇÃO PARA CALCULAR A FREQUÊNCIA DAS FAIXAS
# -------------------------------------------------------------------------
def calcular_frequencias(dados, num_faixas, valor_max=100):
    """Divide os dados em faixas e conta a frequência de cada uma."""
    frequencias = [0] * num_faixas
    if not dados:
        return frequencias
    
    tamanho_faixa = valor_max / num_faixas
    for valor in dados:
        # Força o valor a ficar dentro do limite para evitar erros de índice
        v = min(max(0, valor), valor_max - 1)
        indice = int(v // tamanho_faixa)
        frequencias[indice] += 1
    return frequencias

# Gera cores aleatórias para as faixas de cada histograma de forma genérica
cores_h1 = [(random.randint(50, 250), random.randint(50, 250), random.randint(50, 250)) for _ in range(faixas_h1)]
cores_h2 = [(random.randint(50, 250), random.randint(50, 250), random.randint(50, 250)) for _ in range(faixas_h2)]
cores_h3 = [(random.randint(50, 250), random.randint(50, 250), random.randint(50, 250)) for _ in range(faixas_h3)]

# -------------------------------------------------------------------------
# FUNÇÃO DE RENDERIZAÇÃO DO HISTOGRAMA
# -------------------------------------------------------------------------
def desenhar_histograma(dados, num_faixas, cores, titulo):
    """Desenha o gráfico na tela com eixos, marcações e barras coloridas."""
    # Título do Histograma atual
    txt_titulo = fonte_g.render(titulo, True, COR_TEXTO)
    tela.blit(txt_titulo, (LARGURA // 2 - txt_titulo.get_width() // 2, 40))
    
    # Área do gráfico (Origem do plano cartesiano)
    origem_x = 150
    origem_y = 550
    largura_grafico = 700
    altura_grafico = 400
    
    # Desenha os Eixos X e Y
    pygame.draw.line(tela, COR_EIXO, (origem_x, origem_y), (origem_x + largura_grafico, origin_y), 3) # Eixo X
    pygame.draw.line(tela, COR_EIXO, (origem_x, origem_y), (origem_x, origem_y - altura_grafico), 3) # Eixo Y
    
    frequencias = calcular_frequencias(dados, num_faixas)
    max_freq = max(frequencias) if max(frequencias) > 0 else 10
    
    # Marcações e Linhas do Eixo Y (Frequência / Quantidade)
    num_marcador_y = 5
    for i in range(num_marcador_y + 1):
        valor_y = int((max_freq / num_marcador_y) * i)
        pos_y = origem_y - int((altura_grafico / num_marcador_y) * i)
        
        # Linha horizontal de grade bem suave
        pygame.draw.line(tela, (50, 50, 50), (origem_x, pos_y), (origem_x + largura_grafico, pos_y), 1)
        # Traço de marcação no eixo Y
        pygame.draw.line(tela, COR_EIXO, (origem_x - 5, pos_y), (origem_x, pos_y), 2)
        
        txt_y = fonte_p.render(str(valor_y), True, COR_TEXTO)
        tela.blit(txt_y, (origem_x - 30, pos_y - 8))
        
    # Desenho das Barras e Marcações do Eixo X
    largura_barra = largura_grafico / num_faixas
    tamanho_faixa_valor = 100 / num_faixas
    
    for i in range(num_faixas):
        freq = frequencias[i]
        # Calcula a altura proporcional da barra
        altura_barra = int((freq / max_freq) * altura_grafico)
        
        # Define as coordenadas do retângulo da barra
        x_barra = origem_x + (i * largura_barra)
        y_barra = origem_y - altura_barra
        
        # Desenha a barra se ela tiver elementos
        if freq > 0:
            pygame.draw.rect(tela, cores[i], (x_barra + 4, y_barra, largura_barra - 8, altura_barra))
            
            # Mostra o número exato de elementos no topo da barra
            txt_freq = fonte_p.render(str(freq), True, COR_TEXTO)
            tela.blit(txt_freq, (x_barra + largura_barra//2 - txt_freq.get_width()//2, y_barra - 18))
            
    # Marcações de valores embaixo do Eixo X
    for i in range(num_faixas + 1):
        valor_x = int(i * tamanho_faixa_valor)
        pos_x = origem_x + (i * largura_barra)
        
        pygame.draw.line(tela, COR_EIXO, (pos_x, origem_y), (pos_x,起源_y + 5), 2)
        txt_x = fonte_p.render(str(valor_x), True, COR_TEXTO)
        tela.blit(txt_x, (pos_x - txt_x.get_width() // 2, origem_y + 10))

# -------------------------------------------------------------------------
# LOOP PRINCIPAL DO PROGRAMA
# -------------------------------------------------------------------------
histograma_atual = 1  # Controla qual histograma está ativo no menu (1, 2 ou 3)
rodando = True

while rodando:
    mous_pos = pygame.mouse.get_pos()
    tela.fill(COR_FUNDO)
    
    # Definição visual dos botões do menu interativo (Setas)
    btn_esq_rect = pygame.Rect(50, 320, 50, 50)
    btn_dir_rect = pygame.Rect(900, 320, 50, 50)
    
    # Efeito Hover nos botões de navegação
    cor_b_esq = COR_BOTAO_HOVER if btn_esq_rect.collidepoint(mous_pos) else COR_BOTAO
    cor_b_dir = COR_BOTAO_HOVER if btn_dir_rect.collidepoint(mous_pos) else COR_BOTAO
    
    # Desenha botões de navegação (Setas estilizadas em caixas)
    pygame.draw.rect(tela, cor_b_esq, btn_esq_rect, border_radius=5)
    pygame.draw.rect(tela, cor_b_dir, btn_dir_rect, border_radius=5)
    
    txt_seta_e = fonte_m.render("<", True, COR_TEXTO)
    txt_seta_d = fonte_m.render(">", True, COR_TEXTO)
    tela.blit(txt_seta_e, (btn_esq_rect.x + 18, btn_esq_rect.y + 12))
    tela.blit(txt_seta_d, (btn_dir_rect.x + 20, btn_dir_rect.y + 12))

    # Processamento de Eventos (Cliques, Teclado)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
            
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            # Evento de clique para avançar ou voltar no menu interativo
            if btn_esq_rect.collidepoint(evento.pos):
                histograma_atual = 3 if histograma_atual == 1 else histograma_atual - 1
            elif btn_dir_rect.collidepoint(evento.pos):
                histograma_atual = 1 if histograma_atual == 3 else histograma_atual + 1
                
        elif evento.type == pygame.KEYDOWN and histograma_atual == 3:
            # Captura de inputs do teclado nativos do PyGame apenas para o Histograma 3
            if evento.key == pygame.K_RETURN:
                if input_usuario_texto.strip():
                    try:
                        # Converte o texto separado por vírgula em lista de números inteiros
                        valores = [int(x.strip()) for x in input_usuario_texto.split(",") if x.strip().isdigit()]
                        dados_h3 = valores
                        input_usuario_texto = "" # Limpa a caixa após dar Enter
                    except ValueError:
                        pass
            elif evento.key == pygame.K_BACKSPACE:
                input_usuario_texto = input_usuario_texto[:-1]
            else:
                # Restringe o input apenas para números e vírgulas para facilitar a digitação
                if evento.unicode in "0123456789,":
                    input_usuario_texto += evento.unicode

    # Renderiza o Histograma selecionado no momento
    if histograma_atual == 1:
        desenhar_histograma(dados_h1, faixas_h1, cores_h1, "Histograma 1: Lista Aleatória (Automática)")
        txt_info = fonte_p.render(f"Total de itens gerados: {len(dados_h1)}", True, COR_TEXTO)
        tela.blit(txt_info, (150, 600))
        
    elif histograma_atual == 2:
        desenhar_histograma(dados_h2, faixas_h2, cores_h2, "Histograma 2: Lista Estática com Quantidades Aleatórias")
        txt_info = fonte_p.render(f"Total de itens na soma das faixas: {len(dados_h2)} (Máx permitido: {limite_total_h2})", True, COR_TEXTO)
        tela.blit(txt_info, (150, 600))
        
    elif histograma_atual == 3:
        desenhar_histograma(dados_h3, faixas_h3, cores_h3, "Histograma 3: Input do Usuário (Via PyGame)")
        
        # Desenho da interface gráfica para a caixa de Texto de Input do PyGame
        caixa_input_rect = pygame.Rect(150, 620, 500, 35)
        pygame.draw.rect(tela, COR_CAIXA_TEXTO, caixa_input_rect, border_radius=5)
        pygame.draw.rect(tela, COR_EIXO, caixa_input_rect, 1, border_radius=5)
        
        # Renderiza as instruções e o texto em tempo real conforme o usuário digita
        txt_instrucao = fonte_p.render("Digite números separados por vírgula (ex: 12,45,67,8) de 0 a 100 e aperte ENTER:", True, COR_TEXTO)
        tela.blit(txt_instrucao, (150, 595))
        
        txt_digitado = fonte_m.render(input_usuario_texto, True, COR_TEXTO)
        tela.blit(txt_digitado, (caixa_input_rect.x + 10, caixa_input_rect.y + 5))
        
        # Mostra os valores atualmente plotados no Histograma 3
        txt_valores_atuais = fonte_p.render(f"Dados atuais: {str(dados_h3)}", True, (180, 180, 180))
        tela.blit(txt_valores_atuais, (150, 665))

    pygame.display.flip()

pygame.quit()
sys.exit()
