#Oppgave 2 – Funksjon - Tallgenerering

#Definer en funksjon som lager en fin utskrift med et tilfeldig generert tall mellom 0 og 100
# (husk at du kan benytte random.randrange()). Funksjonen skal ikke ta noen parametere. Eksempelutskrift:

#*********
#***97***
#*********
#Kall denne funksjonen noen ganger.

import random
#import måtte til for å bruke random
def tall():
    tallene =random.randrange(0,101)
    print("***")
    print(tallene)
    print("***")
#def definerer tall, og tallene skal være random, dermed random randrange fra 0-100
#stjerner er for å dekorere og tallene er de random tallene jeg har definert at skal skje når vi kaller tall()
tall()
tall()
tall()
