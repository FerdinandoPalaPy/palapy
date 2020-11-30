stringa1 = "Per quanti giorni ha intenzione di noleggiare uno scooter 50cc?"
stringa2 = "Il prezzo è di"
r1 = 45.00
r2 = 80.00
r3 = 120.00
r4 = 160.00
print(stringa1)
a = int(input("Inserisci il numero di giorni: "))
p_g_extra = r4 + (a-4)*40
if a == 1 :
    print(stringa2, r1, "€")
if a == 2 :
    print(stringa2, r2, "€")
if a == 3 :
    print(stringa2, r3, "€")
if a == 4 :
    print(stringa2, r4, "€")
if a > 4 :
    print(stringa2, p_g_extra, "€")
    



