print("------------------------------------------------")
print("------------- Calculateur de prix --------------")
print("------------------------------------------------\n")

# Assignation des variable
nombre_etiquette_grise = 0
nombre_etiquette_blanche = 0
prix_etiquette_blanche = 1.25
prix_etiquette_grise = 1.50
prix_de_livraison = 0.05
livraison = False

# Demande d'information à l'utilisateur
nombre_etiquette_blanche = int(input("Entrée le nombre d'étiquette blanche : "))
nombre_etiquette_grise = int(input("Entrée le nombre d'étiquette grisse : "))

# Vérifier si l'utilsateur n'aurait pas entré des nombre négatif
if nombre_etiquette_blanche < 0 or nombre_etiquette_grise < 0:
  print("Vous ne pouvez pas entrée de nombre négatif. Le programme va maintenant quitté.")
  quit()

# Récolter l'informaion par rapport au shipping
while True:
  livraison = str(input("Livrer les étiquettes? (o/n): "))
  if livraison == "o":
    livraison = True
    break
  elif livraison == "n":
    livraison = False
    break
  else:
    print("Vous avez entrée un caractère non valide pour la livraison.")

# Calculer le sous-total et le total
nb_etiquette_total = nombre_etiquette_blanche + nombre_etiquette_grise
if livraison == True:
  sous_total = nombre_etiquette_blanche * prix_etiquette_blanche + nombre_etiquette_grise * prix_etiquette_grise + prix_de_livraison * nb_etiquette_total
else:
  sous_total = nombre_etiquette_blanche * prix_etiquette_blanche + nombre_etiquette_grise * prix_etiquette_grise + prix_de_livraison * nb_etiquette_total

print("Sous-total : " + str(sous_total) + "\n" + "Total : " + str(round(sous_total*1.15, 2)))


# Fin
print("Merci d'avoi utiliser le calculateur de prix!")
input("Tapez sur entré pour quitté")