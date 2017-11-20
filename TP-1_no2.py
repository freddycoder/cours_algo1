print("------------------------------------------------")
print("----------------- TP-1 - no.2 ------------------")
print("------------------------------------------------\n")

# Assignation des variable
nb = -1
somme = 0

while nb <= 0:
  nb = int(input("Entre un nombre plus grand ou égal zéro : \n"))
  if nb < 0:
    print("Vous avez entré un nombre négatif.")

# La somme effectué par une boucle
for i in range(0, nb+1):
  somme = somme + i
 
print("La somme est : " + str(somme))

# La somme produit par une équation rapide à résoudre pour le processeur
print("La somme est : " + str(nb*(nb+1)/2))

input("Tapez enter pour quitter …")
