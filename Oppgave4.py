#Oppgave 5 - Småkaker:

#Det følgende er en oversikt over hvor mange småkaker fem forskjellige personer har spist over en uke:

#Person 1: 5 småkaker
#Person 2: 9 småkaker
#Person 3: 2.5 småkaker
#Person 4: 21 småkaker
#Person 5: 0 småkaker
#Beregn det gjennomsnittlige antall spiste småkaker ved å benytte variabler og operatorer. Skriv ut svaret som datatypen, int.

#Gjennomsnittet er beregnet ved å dele det totale antall spiste småkaker på antallet personer.
#Benytte gjerne også en egen variabel for å representere antallet personer.

#Det riktige svaret av utregningen er 7.

person_1=5
person_2=9
person_3=2.5
person_4=21
person_5=0
#her vises personene som har spist kake, og hvor mye de har spist, de var ikke beskjedne!
totalt_spiste_kakestykker=person_1+person_2+person_3+person_4+person_5
#ovenfor her valgte jeg å lage en variabel som summerte opp alle kakestykkene, jeg kunne hatt en print under her dersom jeg var interessert i det antallkaker som var konsumert.

antall_personer_spist_kake= 5

gjennomsnitt= (totalt_spiste_kakestykker/antall_personer_spist_kake)
print(f"Gjennomsnitt spiste kaker:{int(gjennomsnitt)}")
#ovenfor står print som sier at vi sender noe som skal vises i displayet, videre er den det som kalles en f-string som gjør at vi kan kombinere
#tekst med verdier. Videre viser int at vi ønsker at verdien skal være et heltall ikke en float som det kunne blitt.