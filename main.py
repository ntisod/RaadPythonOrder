import utskrift

#mata in personuppgifter
namn = input("ange ditt namn ")
email = input("ange din e-postadress ")

# öppna fil
f = open("orders.txt", "a")

# kod för att göra så att man kan köra programmet ifall man vill
while (True):

  # mata in  beställningar
  ordertyp = input("ange vilken typ av produkt ")
  antalorder = input("ange antal på produkten ")

  # skapa string för att skriva till fil
  text = namn + ";" + email + ";" + ordertyp + ";" + antalorder + "\n"

  # skriv till filen
  f.write(text)
  extraorder = input("vill du beställa en till produkt?(ja/nej) ")
  #frågar om man vill lägga till beställning
  if extraorder.lower() == "nej":
    break
# stäng filen
f.close()
