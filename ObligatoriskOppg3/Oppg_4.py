#Oppgave 4 – Funksjon – Volum

#Lag en funksjon for å regne ut volumet av et tredimensjonalt objekt.
# Vi lar ting være enkelt og forholder oss bare til enkle verdier for lengde, bredde og høyde.
# Volumet kan da beregnes med følgende formel: lengde*bredde*høyde.
# Du skal ta lengden, bredden og høyden som individuelle input-parametere for funksjonen,
# og returnere volumet. Kall funksjonen noen ganger med forskjellige verdier for lengde, bredde og høyde,
# og skriv ut resultatet av hver utregning.

def finne_volum(lengde, bredde, hoyde):
    return lengde * bredde * hoyde

lengde = int(input("Skriv inn lengde: "))
bredde = int(input("Skriv inn bredde: "))
hoyde = int(input("Skriv inn hoyde: "))

volum= finne_volum(lengde, bredde, hoyde)
print(f"Volumet på objektet er {volum}")