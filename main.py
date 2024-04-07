import pygame, os, sys

os.environ['SDL_VIDEO_CENTERED'] = '1'
#open the window in the middle of the screen

#sets resolution
rozliseniObrazovky = (800,1000)

okno = pygame.display.set_mode(rozliseniObrazovky)
pygame.display.set_caption("SPŠsteam") #capiton on top left

#sets fonts
pygame.init()

def FontChoossenSize(font, size):
    return pygame.font.SysFont(font, size)
# returns font with size and name

''' print(pygame.font.get_fonts()) '''
    #prints all availible fonts  

#Images
profilovka = pygame.image.load("C:/Users/Ok I pull up/Desktop/vj/spssteam-napad/profilePicture.png")
profilovka = pygame.transform.scale(profilovka, (100,100))

#colours
lightBlue = (102,140,244) #background
steamBlue = (42,71,94) # top bar color
buttonColour = (24,48,66)

#inputs
jmeno = "Ivan"
#jmeno = input("Zadej svoje jméno: ")[:9]
#character limit of 9


# HRY
#counts all .py fies in the dirrectory bellow
pyCounter = 0
for root, dirs, files in os.walk("C:/Users/Ok I pull up/Desktop/vj/spssteam-napad/HRY"):
    for file in files:
        if file.endswith(".py"):
            pyCounter += 2

listHerRect = []
for pocetHer in range(pyCounter):   
    listHerRect.append(pygame.Rect(40, 120*(pocetHer+1) + 100*(pocetHer+1), 720, 200))
    print(listHerRect)
    
#======================================================LOOP==========================================================================
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()

    stisknuteKlavesy = pygame.key.get_pressed()
    mousePosition = pygame.mouse.get_pos()


    okno.fill(lightBlue)

    topBar = pygame.draw.rect(okno, steamBlue, (0,0, rozliseniObrazovky[1], 110))

    #Renders buttons
    listHerButtonRect = pygame.Rect(30,30, 150,50)
    listHerButton = pygame.draw.rect(okno, buttonColour, listHerButtonRect, 2, 1) #draws box for listHer
    listHerText = FontChoossenSize("Verdana", 29).render("Knihovna", True, (0,0,0)) #renders text
    # True means anti-allising (text won't be jagged)

    leaderboardButtonRect = pygame.Rect(210,30, 150,50)
    leaderboardButton = pygame.draw.rect(okno, buttonColour, leaderboardButtonRect, 2, 1) #draws box for leaderboard
    leaderboardText = FontChoossenSize("Verdana", 22).render("Leaderboard", True, (0,0,0))

    obchodButtonRect = pygame.Rect(390,30, 150,50)
    ObchodButton = pygame.draw.rect(okno, buttonColour, obchodButtonRect, 2, 1) 
    obchodText = FontChoossenSize("Verdana", 29).render("Obchod", True, (0,0,0))

    #TopBar Profile
    okno.blit(profilovka, (560, 5))
    profilovkaRect = pygame.Rect(560, 5, 100,100)
    pygame.draw.rect(okno, (buttonColour), (560, 5, 100, 100), 5, 1) 
    #okraj okolo profilovky

    #profilovka - jméno
    jmenoRect = pygame.Rect(670, 15, 120, 25)
    jmenoFont = FontChoossenSize("Verdana", 20).render(jmeno, True, (0,0,0))
    okno.blit(jmenoFont, (670, 15))

    #RENDERS FONT
    okno.blit(listHerText, (38,37)) #blit listHer text
    okno.blit(leaderboardText, (216, 41))
    okno.blit(obchodText, (407, 37))

    #mouse
    mousePositionRect = pygame.Rect(mousePosition[0]-1, mousePosition[1]-1, 3, 3)
    pygame.draw.rect(okno, (255,0,0), mousePositionRect)

    if event.type == pygame.MOUSEBUTTONUP:
        if pygame.Rect.colliderect(mousePositionRect, listHerButtonRect):
            print("Klikl jsi na Knihovnu")
        elif pygame.Rect.colliderect(mousePositionRect, leaderboardButtonRect):
            print("Klikl jsi na leaderboard")
        elif pygame.Rect.colliderect(mousePositionRect, obchodButtonRect):
            print("Klikl jsi na obchod")
        elif pygame.Rect.colliderect(mousePositionRect, profilovkaRect) or pygame.Rect.colliderect(mousePositionRect, jmenoRect):
            print("Klikl jsi na profil")

    #print(f"X: {mousePosition[0]}   Y: {mousePosition[1]}")


    #boxy pro hry
    for pocetHer in range(pyCounter):
        print(listHerRect)
        pygame.draw.rect(okno, buttonColour, listHerRect[pocetHer], 2, 1)

    if len(listHerRect) > 3:
        vlevoSipkaRect = pygame.Rect(340, 930 ,60 ,60)
        pravoSipkaRect = pygame.Rect(440, 930 ,60 ,60)

        sipkaVlevo = pygame.draw.rect(okno, buttonColour, vlevoSipkaRect, 3 ,1)
        sipkaPravo = pygame.draw.rect(okno, buttonColour, pravoSipkaRect, 3, 1)

    pygame.display.update()