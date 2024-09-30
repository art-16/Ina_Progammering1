#Lag en dictionary med informasjon om en student:



#Skriv ut studentens fullstendige navn (fornavn og etternavn).
#Programmatisk endre studentens favorittkurs til å inkludere kursets emnekode: "ITF10219 Programmering 1"

student = {
    "first name" : "Ola",
    "last name" : "Nordmann ",
    "favourite course" : "Programmering 1"
}
#krollparantesen her definerer at det er dictionary, og dermed er det ordet student som må brukes for å hente verdiene
print("Fulle navn er:" + student["first name"] + " "+ student ["last name"])

student ["favourite course"] = "ITF 10219 Programmering 1"
#Ved å hente endre en verdi må student kalles og skrive dens om skal endres litt som på liste-opplegg
print("Studentens favorittkurs er " + student["favourite course"])

student ["alder"] = 32
#tror det ble rett, valgte å printe student for å se det i consol så det kom opp , så ja :-)
print(student)