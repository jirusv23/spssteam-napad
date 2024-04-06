import pygame, os, sys

os.environ['SDL_VIDEO_CENTERED'] = '1'
#open the window in the middle of the screen

pygame.init()
Verdana29 = pygame.font.SysFont("Verdana", 29)
Verdana22 = pygame.font.SysFont("Verdana", 22)

#sets resolution
rozliseniObrazovky = (800,1000)

okno = pygame.display.set_mode(rozliseniObrazovky)
pygame.display.set_caption("SPŠsteam") #capiton on top left

#print(pygame.font.get_fonts())
#prints all availible fonts

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()

    okno.fill((102,140,244))

    topBar = pygame.draw.rect(okno, (42,71,94), (0,0, rozliseniObrazovky[1], 110))

    listHerButton = pygame.draw.rect(okno, (24,48,66), (30,30, 150,50), 2, 1) #draws box for listHer
    listHerText = Verdana29.render("Knihovna", False, (0,0,0)) #renders text

    leaderboardButton = pygame.draw.rect(okno, (24,48,66), (210,30, 150,50), 2, 1) #draws box for leaderboard
    leaderboardText = Verdana22.render("Leaderboard", True, (0,0,0))

    ObchodButton = pygame.draw.rect(okno, (24,48,66), (390,30, 150,50), 2, 1) 
    obchodText = Verdana29.render("Obchod", True, (0,0,0))

    okno.blit(listHerText, (38,37)) #blit listHer text
    okno.blit(leaderboardText, (216, 41))
    okno.blit(obchodText, (407, 37))

    pygame.display.update()