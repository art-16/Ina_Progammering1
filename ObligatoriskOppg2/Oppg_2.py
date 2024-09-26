#Oppgave 2 - Løkker
#Skriv et program som skriver ut alle oddetall fra og med 9 til 101.
# Lag to alternativer for programmet; en hvor du benytter en for-løkke og hvor du benytter en while-løkke.

print("Skriver ut oddetall fra 9-101")
for tall in range(9,102,2):
    print(tall)

print("Skriver ut det samme men på annen ut måte med while-løkker")
tall = 9
while tall < 102:
    print(tall)
    tall = tall +2
#så den siste linjen forteller meg at det hele tiden skal plusse 2 påhver tall fra 9-101