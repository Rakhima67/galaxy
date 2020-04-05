import pygame
import random
import sys 

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((800, 600))
a=800
b=600

done = False

#LOADING IMAGES

bckgrndImage = pygame.image.load("background.jpg")
gameIcon = pygame.image.load("igrok.png")
vragImage = pygame.image.load("vrag.png")
bombaImage = pygame.image.load("bomba.png")
lifeImage = pygame.image.load("life.png")

#IGROKI
igrok_a = 400
igrok_b = 500
#VRAGI
vrag_a = random.randint(0, 736)
vrag_b = random.randint(20, 50)

bomba_a = 420
bomba_b = 470

life_a = 20
life_b = 10
san = 3
vrag_da = 5
vrag_db = 30
bomba_da = 0
bomva_db = 5
m = bomba_db = 300
n= score =  0
cnt=0
poslIgr_a = 0
#FUNCTIONS

def igrok(a, b):
    screen.blit(gameIcon, (a,b))
def vrag(a, b):
    screen.blit(vragImage, (a,b))
def bomba(a, b):
    screen.blit(bombaImage, (a, b))
def life(a, b):
    screen.blit(lifeImage, (a, b))
def lifely(a,b):
    screen.blit(lifesan, (a,b))
def scores(a,b):
    screen.blit(score, (a,b))
def points(a,b):
    screen.blit(cntn, (a,b))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            done = True
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]: igrok_a -= 3
    if pressed[pygame.K_RIGHT]: igrok_a += 3

    screen.fill((0,0,0))

    vrag_a += vrag_da
    if vrag_a < 0 or vrag_a > 736:
        vrag_da = -vrag_da
        vrag_b += vrag_db
    bomba_a = bomba_a + 20

    if bomba_a == bomba_b+20 and bomba_b==470:
        poslIgr_a = igrok_a

    if pressed[pygame.K_SPACE]:
        bomba_a = poslIgr_a+20
        m=bomba_b

    if m>0:
        bomba_a=poslIgr_a+20
        bomba_b -= bomba_db

    if bomba_b == 0:
        bomba_db = 0
        bomba_a = igrok_a+20
        bomba_b=470
        san-=1

    if pressed[pygame.K_SPACE]:
        bomba_db=5
        bomba_a=poslIgr_a+20
        bomba_b-=bomba_db

    #ubit' vraga
    if bomba_a >= vrag_a and bomba_a <= vrag_a + 64 and bomba_b <= vrag_b + 64:
        vrag_a = random.randint(0, 736)
        vrag_b = random.randint(20, 50)
        bomba_db=0
        bomba_a=igrok_a+20
        bomba_b=470
        cnt+=100
    font = pygame.font.SysFont("arial", 25)

    life = font.render("Life: ", True, (185, 60, 223)) 
    score_a=600
    score_b=10

    cntn = font.render(str(cnt), True, (204, 225, 147))

    cntn_a=750
    cntn_b=10

    over=pygame.font.SysFont("arial", 50)

    #GAMEOVER

    qqq = pygame.font.SysFont("arial", 35)
    if san==3:
        lifesan = qqq.render("3", True, (230, 95, 245))
    if san==2:
        lifesan = qqq.render("2", True, (230, 95, 245))
    if san==1:
        lifesan = qqq.render("1", True, (230, 95, 245))
    if san==0 or vrag_b==igrok_b:
        lifesan = qqq.render("0", True, (230, 95, 245))
        vse = over.render("The game is over", True, (230, 95, 245))
        screen.blit(vse, (400, 300))
        vrag_da=0
        vrag_db=0
        vrag_a=250
        vrag_a=500
        bomba_db=0
        bomba_a=420
        bomba_b=470
        igrok_a=400
        igrok_b=500
        
    lifesan_a=55
    lifesan_b=5
    lifesanRect = lifesan.get_rect()

    screen.blit(bckgrndImage, (0, 0))
    igrok(igrok_a, igrok_b)
    vrag(vrag_a, vrag_b)
    bomba(bomba_a, bomba_b)
    # life(life_a, life_b)
    # lifely(scoresan_a, scoresan_b)
    # scores(score_a, score_b)
    points(cntn_a, cntn_b)

    pygame.display.flip()