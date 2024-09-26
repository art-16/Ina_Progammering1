#Ta et tall fra brukeren på følgende måte: input("Hva er svaret på det ultimate spørsmålet om livet,
# universet og alle ting? Hint: Det er et tall."). Konverter inputen til int og lag en if-test som
# sjekker om verdien er lik 42. Hvis dette er tilfellet, skriv ut "Det stemmer, meningen med livet er 42!",
# hvis ikke; skriv ut "FEIL!".

brukers_tall = input("Hva er svaret på det ulitmate spørsmålet  livet, universet og alle ting? HINT: det er et tall ")
brukers_tall = int(brukers_tall)
if brukers_tall == 42:
    print(f"Det stemmer, meningen med livet er 42")
elif brukers_tall > 30 and brukers_tall < 50:
    print(f"Nærmere, men feil!")
else: print(f"FEIL!")


#Legge til én ekstra sjekk i denne if-testen som sjekker om input-tallet er mellom 30 og 50,
# altså større enn 30 og mindre enn 50 på samme tid (hint: logiske operatorer).
# Hvis dette er tilfellet, skriv ut "Nærme, men feil."

