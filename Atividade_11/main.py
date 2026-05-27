from pygame import *
import sys 


clock = time.Clock()

hero_img = image.load("Atividade_11/assets/Hero_Walk_01.png")

samurai_img = image.load("Atividade_11/pixelArt/samurai/walk.png")

boy_img = image.load("Atividade_11/pixelArt/fighter/Attack_1.png")

run_animation = False
#curr_frame = 0
#anim_time = 0
#hero_walk_list = []

curr_frame = 0
anim_time = 0
boy_fight_list = []


curr_frame_m = 0
anim_time_m = 0
megaman_run = image.load("Atividade_11/megaman_spritesheet.png")

curr_frame_s = 0
anim_time_s = 0
samurai_walk = image.load("Atividade_11/pixelArt/samurai/walk.png")

#for i in range(4):
    #hero_walk_list.append(image.load(f"Atividade_11/assets/Hero_Walk_0{i+1}.png"))


for i in range(4):
    boy_fight_list.append(image.load(f"Atividade_11/pixelArt/Attack_0{i+1}.png"))


init()
screen = display.set_mode((1280,720))
display.set_caption("My Lord")

while True:
    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit()
        if ev.type == KEYDOWN:
            if ev.key == K_d:
                run_animation = True
            #if ev.key == 

    
    clock.tick(60)
    dt = clock.get_time()
    anim_time = anim_time + dt
    anim_time_sec = anim_time/1000

    if anim_time_sec > 0.15:
        curr_frame +=  1
        if curr_frame > len(boy_fight_list) - 1:
            curr_frame = 0
        anim_time = 0
    
    # if run_animation:
    #     anim_time_m = anim_time_m + dt
    #     anim_time_m_sec = anim_time_m/1000
        
    #     if anim_time_m_sec > 0.1:
    #         curr_frame_m +=  1
    #         if curr_frame_m > 9:
    #             curr_frame_m = 0
    #             run_animation = False
    #         anim_time_m = 0
    
    if run_animation:
        anim_time_s = anim_time_s + dt
        anim_time_s_sec = anim_time_s/1000

        if anim_time_s_sec > 0.1:
            curr_frame_s += 1
            if curr_frame_s > 7:
                curr_frame_s = 0
                run_animation = False
            anim_time_s = 0

    

    # Desenho dos elementos na tela
    screen.fill((255,255,255))

    screen.blit(boy_fight_list[curr_frame],(0,0))
    
    # if curr_frame_m < 5:
    #     screen.blit(megaman_run , (200,200), (60 * curr_frame_m,0,60,60))
    # else:
    #     screen.blit(megaman_run,(200,200),(60 * (curr_frame_m - 5 ),0,60,60))

    screen.blit(megaman_run, (200,200), (60*(curr_frame_m%5), 60*(curr_frame_m//5),60,60))

    # if curr_frame_s < 8:
    #     screen.blit(samurai_walk, (0,300), (150 * curr_frame_s,0,150,150))
    # else:
    #     screen.blit(samurai_walk,(0,300),(150* curr_frame_s,0,150,150))
    
    screen.blit(samurai_walk, (300,300),(128*(curr_frame_s%8), 128*(curr_frame_s//8),128,128))

    
    
    
    display.update()

