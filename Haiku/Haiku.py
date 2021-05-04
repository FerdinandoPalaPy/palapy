import random
from guizero import *

def genera_haiku():
    f=open('Haiku1.txt') 
    f2=open('Haiku2.txt')
    f3=open('Haiku3.txt')
    haiku= random.choice(f.readlines())\
    , random.choice(f2.readlines())\
    , random.choice(f3.readlines())
    text = Text(app, text=haiku)
                                                            
app=App(title="Generatore di Haiku")
intro=Text(app, text="Benvenuto su Generatore di Haiku!")
bottone=PushButton(app, text="genera Haiku", command=genera_haiku)
app.display()
