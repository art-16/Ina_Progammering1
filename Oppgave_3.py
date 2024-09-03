#Oppgave 3 - Operatorer:

#Lag en mini-kalkulator.

#Ta to tall som input fra brukeren på en fornuftig måte.

#Basert på de to tallene, skriv ut resultatet av samtlige av de følgende operatorene (Det holder med å skrive ut alle operasjonene etter hverandre, men det er jo alltids lov å gjøre det mer komplisert hvis man vil):

#* (gange)
#/ (dele)
#+ (pluss)
#- (minus)
#% (modulo)
#** (opphøye)
#// (dele med nedrunding

number_1 = int(input("Enter first number:"))
number_2 = int(input("Enter second number:"))
print(f"Addisjon av to nummer: {number_1 + number_2}")
print(f"Subtrahere to nummer: {number_1 - number_2}")
print(f"Multiplisere to nummer: {number_1 * number_2}")

print(f"Dividere to nummere: {number_1 / number_2}")
print(f"Opphøye nummer: {number_1 ** number_2}")
print(f"Nummere i modulo: {number_1 % number_2}")
print(f"Dele med nedrunding: {number_1 // number_2}")