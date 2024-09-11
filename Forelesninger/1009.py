planeter = ["merkur","venus","jorden","saturn","uranus"]
print(planeter)

#slik printer u kun en del av listen:
print(planeter[2])

#Sette inn et element ved å skirve
planeter[3] = "mars"
print(planeter)

#her er en liste med ulike verdier, men en liste inne i seg
random_list = ["Europe",7, ["Ny liste",23,"med nye elementer"], "Bil"]
print(random_list[2])

#men jeg ønsker å få tak i "med nye elementer"
print(random_list[2][1])

#legg til et navn i listen f.eks ina
random_list.append("ina")
print(random_list) #den blir lgt til på slutten

#ønsker man å legge den til på et spess sted må man bruke insert
random_list.insert(1,"ina")
print(random_list)


random_list[2][2] = "forelesning"
print(random_list)