print("------------------------------------------------")
print("----------------- TP-1 - no.5 ------------------")
print("------------------------------------------------\n")

nb_jour_mois = int(input("Entrer le nombre de jour dans le mois. Doit être entre 28 et 31\n"))
premier_jour_semaine = int(input("Enter quel est le premier jour de la semaine. Exemple 1 pour dimanche, 2 pour lundi... et 7 pour samedi\n"))

if nb_jour_mois > 31 or nb_jour_mois < 28 or premier_jour_semaine < 0 or premier_jour_semaine > 7:
  input("Le programme va quitter car vous avez entrer des données non valide. \nAppuyer sur entrée pour sortire")
  quit()

print("Voici le calendrier :\n D  L  M  M  J  V  S")
print("   " * (premier_jour_semaine-1), end="")

i = 1
premiere_fois = True

while i < nb_jour_mois:
  if premiere_fois == True:
    premiere_fois = False
    for row in range(premier_jour_semaine, 8):
      print(" " + str(i) + " ", end="")
      i = i + 1
  else:
    for row in range(1, 8):
      if i > nb_jour_mois:
        break
      elif i > 9:
        print(" " + str(i), end="")
        i = i + 1
      else:
        print(" " + str(i) + " ", end="")
        i = i + 1
  print()
