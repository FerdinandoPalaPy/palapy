import random
from guizero import *

def genera_haiku():	
    f=open('Haiku1.txt') 
    f2=open('Haiku2.txt')
    f3=open('Haiku3.txt')
    haiku1=random.choice(f.readlines())
    haiku2=random.choice(f2.readlines())
    haiku3=random.choice(f3.readlines())
    listbox= ListBox(app, width=150, height=55, items=[haiku1, haiku2, haiku3])
    
app=App(title="Generatore di Haiku")
intro=Text(app, text="Benvenuto su Generatore di Haiku!")
bottone=PushButton(app, text="Genera Haiku", command=genera_haiku)
app.display()
