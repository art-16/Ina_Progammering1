planeter = ["Merkur", "Venus", "Jorden", "Mars", "Jupiter", "Saturn", "Uranus", "Neptun"]
tyngdekraft = [3.7, 8.87, 9.807, 3.721, 24.79, 10.44, 8.87, 11.5]

print("---Planeter---")
print("1 - Merkur")
print("2 - Venus")
print("3 - Jorden")
print("4 - Mars")
print("5 - Jupiter")
print("6 - Saturn")
print("7 - Uranus")
print("8 - Neptun")

planetnummer = int(input("Velg et planetnummer: "))
#int i forkant her sier at dersom brukeren skriver en vil det blir gjort om til 1

#Nå skriver vi en tekst eller en if test som tester at brukeren legger inn det rett, eller så avbryter programmet

if(planetnummer <= 0 or planetnummer > len(planeter)):
    #denne if testen over her på venstre side sier om tallet er over null og  høyre sdise av or om brukeren har skrevet inn for høyt tallom brukeren skriver inn tall mellom 0 og 8
#så hvis den gjør det såprinter vi følgende:
    print("Nummeret er ikke gyldig")
    exit()

#Vi må gjøre om 1-0 og osv fordi de tallet skal nyttes til planetnummer
planetnummer=planetnummer - 1
print(f"Du valgte planeten {planeter[planetnummer]}")

din_vekt = input("Hva er din vekt på jorden?(i hele kg)")
#denne vil bli tolket som en string så vi kan endre den ved å
din_vekt = int(din_vekt) #her har du fått inn at om brukeren friver søtti vil det bli 70

din_masse = din_vekt / tyngdekraft[2]
vekt_paa_planet = din_masse * tyngdekraft[planetnummer]

print(f"Din vekt på {planeter[planetnummer]} er {round(vekt_paa_planet,2)}kg")
#denne ovenfor her sier mye greier, men round er for å runde a så vi ikke får så mange desimaler.
#Ina husk at når du kjører er det forskjell på å tykke play og  å trykke enter i konsollen
#NOTE at du har endret farge