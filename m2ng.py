import pygame, sys, random
pygame.init()
pygame.mixer.music.load("muusika.mp3")
pygame.mixer.music.play(-1)
font = pygame.font.Font(None,25)             
a = pygame.display.set_mode((400,250))
k = pygame.image.load("kosmonaut.png")
l = pygame.image.load("lepatriinu.png")
lp = pygame.image.load("lepatriinup.png")                 
k = pygame.transform.scale(k,(40,50))
l = pygame.transform.scale(l,(50,50))
lp = pygame.transform.scale(lp,(50,50))
logo = pygame.transform.scale(l,(50,50))
pygame.display.set_caption("Kosmonaudi mäng: EkstraHullus")
pygame.display.set_icon(logo)
kx = 160
ky = 200
hüppamine = False
pv = False, False
ll = False
punktid = 0
kiirus = 1
while True:
    a.fill((0,0,100))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP:
                ky = 150
                stopper = 0
                hüppamine = True
            elif e.key == pygame.K_RIGHT:
                pv = True, False
            elif e.key == pygame.K_LEFT:
                pv = False, True
            elif e.key == pygame.K_DOWN:
                hüppamine = False
                ky = 200
            elif e.key == pygame.K_SPACE:
                pausil = True
                kiri = font.render("PAUSIL",1,(225,225,225))
                a.blit(kiri,(200,0))
                if ll:
                    if llp:
                        a.blit(l,(lx,200))
                    else:
                        a.blit(lp,(lx,200))
                a.blit(k,(kx,ky))
                kiri = font.render(tekst,1,(225,225,225))
                a.blit(kiri,(0,0))
                pygame.display.flip()
                pygame.mixer.music.pause()
                while pausil:
                    for e in pygame.event.get():
                        if e.type == pygame.KEYDOWN:
                            if e.key == pygame.K_SPACE:
                                pausil = False
                        elif e.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit
                pygame.mixer.music.unpause()
        elif e.type == pygame.KEYUP:
            if e.key == pygame.K_LEFT or e.key == pygame.K_RIGHT:
                pv = False, False
    if pv == (True, False):
        kx += 4
        if kx > 350:
            kx -= 4
    elif pv == (False, True):
        kx -= 4
        if kx < 0:
            kx += 4
    if hüppamine:
        if stopper == 500:
            hüppamine = False
            ky = 200
        else:
            stopper += 10
    if ll == False:
        if random.randint(1,250) == 2:
            ll = True
            llp = True
            lx = 360
            a.blit(lp,(lx,200))
        elif random.randint(1,250) == 4:
            ll = True
            llp = False
            lx = 0
            a.blit(l,(lx,200))
    else:
        if hüppamine == False and abs(lx-kx) <= 25:
            kiri = font.render("Mäng läbi!",1,(255,255,255))
            a.blit(kiri,(0,0))
            pygame.display.flip()
            pygame.time.delay(2500)
            pygame.quit()
            sys.exit()
        if llp:
            lx -= kiirus
            a.blit(l,(lx,200))
        else:
            lx += kiirus
            a.blit(lp,(lx,200))
        if (llp == False and lx > 400) or (llp and lx < 0):
            ll = False
            punktid += 1
    tekst = str(("Punkte", punktid, "Tase", kiirus))
    kiri = font.render(tekst,1,(255,255,255))
    a.blit(kiri,(0,0))
    a.blit(k,(kx,ky))
    if punktid >= 10 and punktid % 10 == 0:
        kiirus += 1
        kiri = font.render("Järgmine tase +1p",1,(255,255,255))
        a.blit(kiri,(200,0))
        pygame.display.flip()
        punktid += 1
        pygame.time.delay(1000)
    pygame.display.flip()
    pygame.time.delay(10)
