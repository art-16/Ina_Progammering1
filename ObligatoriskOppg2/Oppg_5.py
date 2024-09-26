#Oppgave 5 - for-løkke(r) - Dart

#I denne oppgaven skal du simulere et dartspill.
# Det skal kastes 3 piler. Hvert kast gir mellom 0 og 60 poeng. Du kan bruke randrange(<fra>, <til>)
# for å generere en tilfeldig score for hvert kast. For mer info angående randrange, se her

#Links to an external site.. Skriv ut sluttscoren.
#Utvid oppgaven til å ta som input hvor mange spillere som skal spille.
# Hver spiller skal kaste 3 piler hver. Spilleren skal kaste alle 3 pilene før neste spiller skal kaste.
# Skriv ut resultat for hver spiller når spilleren er ferdig med å kaste.


import random
spillere = int(input("Hvor mange ska spille?"))

for spillere in range(1, spillere + 1):
    print(f"Spiller {spillere} sin tur")

piler = 3
total_poeng = 0
for kasting in range(piler):
     poeng = random.randrange(0,61)
     total_poeng += poeng
     print(f"Kasting {kasting + 10} = {poeng} poeng")
#for å skrive ut toalten
print(f"Total poeng etter {piler} er kasta er: {total_poeng}")

#denne var litt too hard for my, måtte få litt hjelp av google, og khan academy, som jeg dermed bruker som referanse.