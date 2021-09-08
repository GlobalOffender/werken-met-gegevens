croissant = 17
croissantprijs = 0.39
stokbrood = 2
stokbroodprijs = 2.78
korting = 1.50
bedrag = (croissant * croissantprijs) + (stokbrood * stokbroodprijs) - korting
text = 'De feestlunch kost je bij de bakker ' + str(bedrag) + ' euro voor de 17 croissantjes en de 2 stokbroden als de 3 kortingsbonnen nog geldig zijn!'

print(text)