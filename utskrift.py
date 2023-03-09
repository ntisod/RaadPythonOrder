f = open("orders.txt")

for x in f:
  namn, email, ordertyp, antalorder = x.split(";")
  print("namn:", namn, "\nemail:", email, "\nprodukt:" ,ordertyp, "\nantal:", antalorder)