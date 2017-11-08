print("------------------------------------------------")
print("----------------- TP-1 - no.5 ------------------")
print("------------------------------------------------\n")

nb_jour_mois = int(input("Entrer le nombre de jour dans le mois. Doit être entre 28 et 31\n"))
premier_jour_semaine = int(input("Enter quel est le premier jour de la semaine. Exemple 1 pour dimanche, 2 pour lundi... et 7 pour samedi\n"))

if nb_jour_mois < 31 or nb_jour_mois > 28 or premier_jour_semaine > 0 or premier_jour_semaine < 7:
  print("Voici le calendrier :\n D  L  M  M  J  V  S")
  print("   " * (premier_jour_semaine-1), end="")

  jour = 1
  premiere_fois = True

  while jour < nb_jour_mois:
    if premiere_fois == False:
      print()
      for row in range(1, 8):
        if jour > nb_jour_mois:
          break
        elif jour > 9:
          print(" " + str(jour), end="")
          jour = jour + 1
        else:
          print(" " + str(jour) + " ", end="")
          jour = jour + 1

    else:
      premiere_fois = False
      while premier_jour_semaine-1+jour < 8:
        print(" " + str(jour) + " ", end="")
        jour = jour + 1
       
else:
  input("Le programme va quitter car vous avez entrer des données non valide. \nAppuyer sur entrée pour sortire")
