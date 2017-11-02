print("------------------------------------------------")
print("----------------- TP-1 - no.3 ------------------")
print("------------------------------------------------\n")

somme = 0
produit = 1

nb_de_nb = int(input("Enter le nombre de de nombre total"))

for i in range(0, nb_de_nb):
  nb = -1
  while nb < 0:
    nb = int(input("Entrer un nombre le nombre " + str(i + 1) + " , il doit être plus grand que 0\n"))
  somme = somme + nb
  produit = produit * nb



print("La somme est " + str(somme))
print("Le produit est " + str(produit))
print("La moyenne est " + str(somme/nb_de_nb))
