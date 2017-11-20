print("------------------------------------------------")
print("----------------- TP-1 - no.3 ------------------")
print("------------------------------------------------\n")

somme = 0
produit = 1

nb_de_nb = int(input("Enter le nombre de de nombre total. Doit être plus grand que 0 : "))

if nb_de_nb > 0:
  for i in range(0, nb_de_nb):
      nb = -1
      while nb < 0:
        nb = int(input("Saisie " + str(i + 1) + ": "))
        if nb > 0:
          somme = somme + nb
          produit = produit * nb
        else:
          print("Le nombre doit être plus grand que zéro.")


  print("La somme est " + str(somme))
  print("Le produit est " + str(produit))
  print("La moyenne est " + str(somme/nb_de_nb))
else:
  print("Vous avez entrée des données non valides. Le programme va maintenant quitter.")
