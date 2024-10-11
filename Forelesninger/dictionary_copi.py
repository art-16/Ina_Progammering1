#oppretter en dictonary med 3 key valuer
brettspill = {
    'tittel' : "Dixit",
    'spilletid' : 30,
    'aldersgrense' : 8
}

#skriver ut lista
#print(brettspill)
#print()

print(brettspill['spilletid'])
print()

#nedenfor endrer vi verdien som er i spiller til fra 30 til 40
brettspill['spilletid'] = 40
print((brettspill))
