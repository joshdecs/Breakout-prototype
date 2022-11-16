from tkinter import *
from turtle import color
from random import *

def deplacement():
    global dx, dy
    if MonCanevas.coords(balle)[3]>400:
        dy=-1*dy
    if MonCanevas.coords(balle)[3]<5:
        dy=-1*dy
    if MonCanevas.coords(balle)[2]>500:
        dx=-1*dx
    if MonCanevas.coords(balle)[2]<5:
        dx=-1*dx
    #On deplace la balle :
    MonCanevas.move(balle,dx,dy)
    #On repete cette fonction
    MaFenetre.after(20,deplacement)
 
#Deplacements balle
dx=5
dy=5
 
#Creation fenetre/canevas
MaFenetre = Tk()
MonCanevas = Canvas(MaFenetre,width = 500, height = 400 , bd=0, bg="white")
MonCanevas.pack(padx=10,pady=10)
 
#Creation bouton "Quitter"
Bouton_Quitter=Button(MaFenetre, text ='Quitter', command = MaFenetre.destroy)
#Affichage bouton fenêtre tk
Bouton_Quitter.pack()
 
#Creation balle
balle = MonCanevas.create_oval(60,10,80,30,fill='blue')
 
deplacement()
 
#Boucle principale:
MaFenetre.mainloop()