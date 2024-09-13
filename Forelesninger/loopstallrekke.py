#Vi skal skrive ut en tallrekke
for tall in range(11):
    print(tall)
#Range funksjonen starter på null, og parameter er 11 inne i prarantes, tall-ordet vil få verdien 0,
#og den vil plusse på 1 helt frem til 10 og tall får da verdien 11, men range teller kun til verdien og vils toppe på 10

for tall in range(1,10):
    print(tall)
#Dette er en egen løkke og henter ikke tall som en variabel på for løkken ovenfor.
#men her kommer ikke null, fordi vi skrev to parameter i rangen at vi ville starte på 1 og slutte på 10, dermed 9

for tall in range(1000,9002,1000):
    print(tall)
#Her har vi start tallet i paramteret som er 1000 og sluttallet 9002 og at på hvert 1000 skal printes
#da får vi printet ut 2000, 3000, 4000 osv

nummere=[]

#men om jeg har mange tall jeg vil fylle inn som i en liste da kan vi:
for tall in range(1000,9002,1000):
    print(tall)
    nummere.append(tall)
    #her brukes tall, og append
print(nummere)
#ikke innrykk her fordi vi vil se alt, hvis jeg glemmer inrykk vil det bli som nedenfor

for tall in range(1000,9002,1000):
    print(tall)
    nummere.append(tall)
    print(nummere)
    #lista vil vokse for hver iterasjon /repeitsjon

#finne laveste versjon av lista vår:
print(min(nummere))
#eller høyest
print(max(nummere))
#printe summen er
print(sum(nummere))