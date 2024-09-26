# Oppgave 3 - Lister

# Opprett en liste med Tolkien sine bøker:

#   The Hobbit
#   Farmer Giles of Ham
#   The Fellowship of the Ring
#   The Two Towers
#   The Return of the King
#  The Adventures of Tom Bombadil
# Tree and Leaf

# Skriv ut de to første og de to siste bøkene i listen.
# Legg til to av bøkene som ble utgitt etter hans død:
#    The Silmarillion
#   Unfinished Tales



tolkin = ["The Hobbit", "Farmer Giles of Ham", "The Fellowship of the Ring", "The Two Towers", "The Return of the King",
          "The Adventures of Tom Bombadil", "Tree and Leaf"]
print("Skriv ut tolkin listen som i oppgaven:")
print(tolkin)


print(f"\nHer er de to første i listen: {tolkin[0]} og {tolkin[1]},\n de to siste på  listen er {tolkin[5]} {tolkin[6]}\n")
tolkin.append("The Silmarillion")
tolkin.append("Unfinished Tales")

print("Her er tolkin listen med de to som ble gitt ut etter hans død, brukt append")
print(tolkin)
#\n gir linedeling, måtte google det for jeg synes det ble ryddligere slik.

 # Gjør endringer på de tre bøkene i Lord of the Rings trilogien og legg til
# "Lord of the Rings: " foran hver av dem. (hvis dere ikke vet hvilke dette er, vet Google)
 # Sorter lista og skriv den ut.
 #Skjønte ikke helt denne siste men prøver
tolkin[2] = "Lord of the Ring: The fellowship of the Ring"
tolkin[3] = "Lord of teg rings: The Two Towers"
tolkin[4] = "Lord of teg rings: The Return of the King"
tolkin.sort()
print("Sortert liste:")
print(tolkin)

 





