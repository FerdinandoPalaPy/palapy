#primo esercizio
a = int(input("inserisci il valore di a: "))
b = int(input("inserisci il valore di b: ")) 
equazione = "ax+b=0"
print(equazione)
x = -b/a
print("x è uguale a: ", x)

#secondo esercizio
c = int(input("inserisci il valore di c: "))
d =max(a, b, c)
print("il numero maggiore tra ", a, ",", b, ",", c, "è: ", d) 

#terzo esercizio
a, b = b, a
print("a = ", a)
print("b = ", b)
