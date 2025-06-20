import pygame
pygame.init ( )
x4 =3
y4 = 500 // 2 
menu = pygame.image.load("pygame\\menu.jpg") # меню 
menu1 = pygame.transform.scale (menu,(500,500))
font = pygame.font.SysFont ("Arial" , 18)
font1 = font.render("Начать новую игру: N",True,"BLue")
f1 = pygame.font.SysFont("Arial",18)
f2 = f1.render("Выход: Q",True,"Blue") 
k = font.render("Управление: K" , True , "Blue" ,)
k1 = font.render("лететь вправо: d " , True , "Black" ,)
k2 = font.render("лететь влево: a " , True , "Black" ,)
k3 = font.render("стрелять: space " , True , "Black" ,)

def f (self):
    global menu , font , font1 
    self.blit(menu1,(0,0))
    self.blit(font1,(x4,y4))
    self.blit(f2,(x4,y4+30))
    self.blit(k,(x4,y4 + 60))
def keyboard (self) :
    self.blit(menu1,(0,0))
    self.blit(k1,(100,y4 ))
    self.blit(k2,(100,y4 + 30 ))
    self.blit(k3,(100,y4 + 60 ))



    
