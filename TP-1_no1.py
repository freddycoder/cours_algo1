print("------------------------------------------------")
print("------------- Calculateur de prix --------------")
print("------------------------------------------------\n")

# Assignation des variable
prix_etiquette_blanche = 1.25
prix_etiquette_grise = 1.50
prix_de_livraison = 0.05
livraison = ""

# Demande d'information à l'utilisateur
nombre_etiquette_blanche = int(input("Entrer le nombre d'étiquettes blanches : "))
nombre_etiquette_grise = int(input("Entrer le nombre d'étiquettes grises : "))

# Vérifier si l'utilsateur à rentrée des données valide.
if nombre_etiquette_blanche > 0 and nombre_etiquette_grise > 0:
  # Récolter l'informaion par rapport au shipping
  while livraison != "n" and livraison != "o":
    livraison = input("Livrer les étiquettes? (o/n): ")
  # Calculer le sous-total et le total
  if livraison == "o":
    nb_etiquette_total = nombre_etiquette_blanche + nombre_etiquette_grise
    sous_total = nombre_etiquette_blanche * prix_etiquette_blanche + nombre_etiquette_grise * prix_etiquette_grise + prix_de_livraison * nb_etiquette_total
  else:
    sous_total = nombre_etiquette_blanche * prix_etiquette_blanche + nombre_etiquette_grise * prix_etiquette_grise
  print("\nSous-total : " + str(sous_total) + "\n" + "Total : " + str(round(sous_total*1.15, 2)))

else:
  print("Vous ne pouvez pas entrer de nombre négatif. Le programme va maintenant terminer.")
  
# Fin
input("Merci d'avoir utilisé le calculateur de prix!\nTapez sur entrée pour quitter le programme.")
