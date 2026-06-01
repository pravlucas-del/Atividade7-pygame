from pygame import *
import sys

init()
screen = display.set_mode((1280,720))
display.set_caption("Mapa inicial")

clock = time.Clock()

tile_size = 60

mapa = []

while True:
    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit()
    
    clock.tick(60)
    dt = clock.get_time()

    # Primeiro Mapa
    for i in range(len(mapa)): # Para cada Linha
        for j in (len(mapa[i])): # Para cada Coluna
            if mapa[i][j] == "G":
                draw.rect(screen,(39,153,0), (tile_size*j, tile_size*i,tile_size,tile_size))
            if mapa[i][j] == "P":
                draw.rect(screen, (230,235,134),(tile_size*j, tile_size*i, tile_size,tile_size))
            if mapa[i][j] == "A":
                draw.rect(screen,(63,125,232), (tile_size*j, tile_size*i,tile_size,tile_size))
    
    
    display.update()
    clock.tick(60)