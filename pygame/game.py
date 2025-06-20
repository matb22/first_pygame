#реализовать главное меню 

import random , main_menu  , pygame

from main_menu import * 
pygame.init( )

#логика игры ниже -> 




x = random.randint (5,295) # враг 
y = 0 # вражеский 
xenemy = random.randint (5,295)
yenemy = 0 
x1 = 300 # окно  
y1 = 500 # окно 
x2 = 150 # игрок 
y2 = 250 # игрок 
x3 = 150 # снаряд 
y3 = 252 # снаряд 
icony = 0 # для пули 
a = 0  # счёт игрока 
a1 = 0 # для выключения выстрела 
a4 = 0 # для выключания найстроек клавиатуры 
a3 = 0 # счёт проигрышей 
font5 = pygame.font.SysFont("Arial",20) # счёт
text = pygame.font.SysFont("Arial",20) # счёт проигрышей 

window = pygame.display.set_mode((x1,y1))
pygame.display.set_caption ("Игра by Юрий for работа")
over = False 
game1 = False # меню 
keyb = False # клавиатура 
fire_gun = False # выстрел 
clock = pygame.time.Clock( )


background_image = pygame.image.load("pygame\\menu.jpg") # задний план (надо сделать гифку)
bulet_icon = pygame.image.load("pygame//Bulet.png") # патрон 
player_image = pygame.image.load("pygame//starboat.png") # игрок , здесь понгятно 
boat =  pygame.image.load ("pygame//космолёт.png").convert_alpha() # враждебный корабль 


# логика игры выше ->



while over is False : # флаг на овер 
    pygame.display.flip ( )
    clock.tick(60)
    font6=  font5.render(f"Счёт:{a}" , True , "Blue") # счёт 
    text1 = text.render(f"осталось:{a3}/3",True, "Blue") # счёт проигрышей 
     
    for i in pygame.event.get( ):
        if i.type == pygame.QUIT :
            over = True 
        if i.type == pygame.KEYDOWN :
                if i.key == pygame.K_n :
                        game1 = True 
                        a3 = 0 
                        a = 0 
                if i.key == pygame.K_q : 
                        over = True 
                if i.key == pygame.K_SPACE : 
                    fire_gun = True 
                    a1 += 1
                    if a1 % 2 == 0 : # для того ,чтобы ,нажав ещё раз отключалось 
                        fire_gun = False 
                if i.key == pygame.K_k :  
                    keyb = True
                    a4 += 1 
                    if a4 % 2 == 0 : 
                        keyb = False 
                  
    if game1 is False : # меню 
        main_menu.f (window)
    if game1 is True :  # фул игра                               
        def enemy ( ) : 
                                    global boat ,  boat1 , boat2 , boat3 ,boat_new ,xenemy ,yenemy, x ,y , a3 ,a 
                                    boat2 = pygame.transform.scale(boat,(30,30))
                                    boat3 = pygame.transform.rotate(boat2,180)
                                    boat1 = boat3.get_rect(center=(x,y))
                                    boat_new = boat3.get_rect(center=(xenemy,yenemy))
                                    boat3.set_colorkey("White")
                                    
                                    window.blit(boat3,boat1)
                                
                                    y += 2 
                                    
                                    if y >= y1 : # первый шатл
                                        y = 0 
                                        x = random.randint(0,x1)
                                        a3 += 1
                                    
                                    if a > 10 : 
                                        y+= 1
                                        yenemy += 1 
        def player ( ) : 
                                        global x2 , x1 , y2 , player_image , player_image1 , player_image2 
                                        player_image2 = pygame.transform.scale(player_image , (30,30))
                                        player_image1 = player_image2.get_rect(center = (x2,y2))
                                        
                                        window.blit(player_image2,player_image1)
                                        walk()
                                        if x2 < 0 : 
                                            x2 = x1
                                        elif x2 > x1 : 
                                            x2 = 0 
        def walk ( ): # player 
                                    global pressed , x2 , y3 
                                    pressed = pygame.key.get_pressed( )
                                    if pressed [pygame.K_d] : x2 += 2
                                    if pressed [pygame.K_a] : x2 -= 2 
                                    if pressed [pygame.K_LSHIFT] and pressed[pygame.K_d] : x2 += 4 
                                    if pressed [pygame.K_LSHIFT] and pressed[pygame.K_a] : x2 -= 4 
                                    
                                             
        
        
             
        image1 = window.blit(background_image,(0,0))
        window.blit(font6 , (0,y1//2))
        window.blit(text1,(0,y1//2 + 20) )
        enemy ( )
        player ( )
        if a3 == 3 :
            game1 = False 
    if fire_gun is True : 
        def fireball ( ): 
                                        
                                        
                                        global y3 , y1 , x3 , icon1 , icon2 ,a , boat1 , x , y 
                                        
                                        x3 = x2
                                        icon2 = pygame.transform.rotate(bulet_icon,60) # преобразования fireball
                                        icon2 = pygame.transform.scale(bulet_icon , (20, 20))
                                        icon1=  icon2.get_rect (center=(x3,y3)) 
                                        
                                        
                                        window.blit(icon2,icon1) 
                                        y3 -= 10 # летит пуля
                                        if y3 <= 0 : 
                                            y3 = 260  
                                        if  icon1.right > boat1.left and \
                                            icon1.left < boat1.right and \
                                            icon1.bottom > boat1.top and \
                                            icon1.top < boat1.bottom:
                                            a += 1 
                                            y = 0 
                                            x = random.randint (5,295)
        fireball ( )                        
    if keyb is True :  # настройки клавы 
        main_menu.keyboard (window)




        