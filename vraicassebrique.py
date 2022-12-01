# on rajoute random
import pyxel, random

# taille de la fenetre 128x128 pixels
# ne pas modifier
pyxel.init(300, 300, title="Josh")

# position initiale du vaisseau
# (origine des positions : coin haut gauche)
vaisseau_x = 125
vaisseau_y = 250
color=6
colorb = 10
score= 0
cox = 50
coy = 100
r=3
x= vaisseau_x + 25
y= vaisseau_y - (r+1)
balle = False
vb = score/4+5
xx=-vb
yy=-vb
velocity = 5
briquehauteur = 10
briquelargeur= 20

#brique
x1=50
x2=75
x3=100
x4=125
x5=150
x6=175
x7=200
x8=225
y1=100
y2=120
brique_liste = []
xdebrique = [x1,x2,x3,x4,x5,x6,x7,x8]
ydebrique = [y1, y2]
brique_debut = True

# vies et score
vies = 3
score= 0


def brique_creation(brique_liste) :
    brique_liste.append([x0,y0])
    return brique_liste

def vaisseau_deplacement(x, y):
    """déplacement avec les touches de directions"""

    if pyxel.btn(pyxel.KEY_RIGHT):
        if (x < 240) :
            x = x + velocity
    if pyxel.btn(pyxel.KEY_LEFT):
        if (x > -20) :
            x = x - velocity

    return x, y


def balle_deplacement():
    global x, y, xx, yy, vies, balle , score , brique_liste , brique
    x += xx
    y += yy
    # Bord gauche

    if x <= r:
        xx = -xx
    # Plafond
    elif y <= r :
        yy = -yy
    # bord droit
    elif x >= 300-r :
        xx = -xx
    # dessus raquette
    elif y >= vaisseau_y-r and y <= vaisseau_y+r and x >= vaisseau_x-r and x <= vaisseau_x+50+r :
        yy = -yy
        score+=10
    # raquette gauche
    elif x >= vaisseau_x-50-r and x <= vaisseau_x+r and y >= vaisseau_y - r and y <= vaisseau_y + 20 - r and pyxel.pget(x+xx, y+yy) == 2 :
        yy = -yy
        score+=20
    # raquette droite
    elif x >= vaisseau_x+50-r and x <= vaisseau_x+100+r and y >= vaisseau_y - r and y <= vaisseau_y + 20 - r and pyxel.pget(x+xx, y+yy) == 2 :
        yy = -yy
        score+=30
    # bas
    elif y >= 300+r :
        balle=False
        xx=-vb
        yy=-vb
        vies = vies-1
        pyxel.text(vaisseau_x,vaisseau_y+10, 'Une vie de moins !', 7)
    # brique 
    for brique in brique_liste :
        if pyxel.pget(x+xx, y+yy) == 10 :
            yy = -yy
            if (y - r + yy) <= (brique[1] + briquehauteur) and (x + r + xx) >= brique[0] and (x - r + xx) <= (brique[0] + briquelargeur):
                brique_liste.remove(brique)
            
            
    #elif pyxel.pget(x+xx, y+yy) == 9 :
            #pyxel.fill(x+xx, y+yy, 8 )
            #yy = -yy
    #elif pyxel.pget(x+xx, y+yy) == 8 :
            #pyxel.fill(x+xx, y+yy, 0 )
            #yy = -yy
            #score += 20
        
   
        
        
        






def brique_suppression():
    """disparition d'un ennemi et d'un tir si contact"""

    #for ennemi in ennemis_liste:
        #for tir in tirs_liste:
            #if ennemi[0] <= tir[0]+1 and ennemi[0]+8 >= tir[0] and ennemi[1]+8 >= tir[1]:
                #ennemis_liste.remove(ennemi)
                

# =========================================================
# == UPDATE
# =========================================================
def update():
    """mise à jour des variables (30 fois par seconde)"""

    global vaisseau_x, vaisseau_y, x, y, balle, brique_liste, vies , x0 , y0

    # mise à jour de la position du vaisseau
    vaisseau_x, vaisseau_y = vaisseau_deplacement(vaisseau_x, vaisseau_y)
    
    if pyxel.btnr(pyxel.KEY_SPACE):
        balle = True

    if balle is False:
        x = vaisseau_x + 25
        y = vaisseau_y - (r+1)
    else:
        balle_deplacement()

    # creation des ennemis
    
    if brique_debut:
        for o in ydebrique :
            for m in xdebrique :
                x0 = m
                y0 = o
                brique_creation(brique_liste)
        brique_debut is False
            
            

    # suppression des ennemis et tirs si contact
    brique_suppression()

    # suppression du vaisseau et ennemi si contact
    

# =========================================================
# == DRAW
# =========================================================
def draw():
    """création des objets (30 fois par seconde)"""

    # vide la fenetre
    pyxel.cls(0)

    # si le vaisseau possede des vies le jeu continue
    if vies > 0:    
        global cox, coy , brique_liste, brique_debut
        # vaisseau 
        pyxel.rect(vaisseau_x, vaisseau_y, 50, 20, 2)
        pyxel.tri(vaisseau_x, vaisseau_y, vaisseau_x, vaisseau_y+20, vaisseau_x-50,vaisseau_y+20,2) 
        pyxel.tri(vaisseau_x+50, vaisseau_y, vaisseau_x+50, vaisseau_y+20, vaisseau_x+100,vaisseau_y+20,2) 
        pyxel.rect(vaisseau_x-50, vaisseau_y+20, 150, 5, 2)

        # tirs
        pyxel.circ(x,y,r,color)
        
        pyxel.text(250,10, 'Score: %d' % score, 7)

        pyxel.text(250,20, 'Vies: %d' % vies, 7)

        # briques
        
        for brique in brique_liste :
            pyxel.rect(brique[0],brique[1], briquelargeur, briquehauteur, colorb)
        
            
            
            
    # sinon: GAME OVER
    else:

        pyxel.text(50,64, 'GAME OVER', 7)

pyxel.run(update, draw)