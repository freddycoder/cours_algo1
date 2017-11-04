print("------------------------------------------------")
print("----------------- TP-1 - no.2 ------------------")
print("------------------------------------------------\n")

# Assignation des variable
nb = -1
somme = 0

while nb <= 0:
  nb = int(input("Entre un nombre plus grand ou egual zero\n"))
  if nb < 0:
    print("Vous avez entrer un nombre negatif")

# La somme effectuer par une boucle
for i in range(1, nb+1):
  somme = somme + i
print("La somme est : " + str(somme))

# La somme produit par une équation rapide à résoudre pour le processeur
print("La somme est : " + str(int(nb*(nb+1)/2)))

input("Tapez enter pour quitter")
