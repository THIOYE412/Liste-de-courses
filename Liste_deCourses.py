# LISTE DE COURSES

liste = []

# Boucle principale

while True:
	print("""
Choisissez parmi les 5 options suivantes :
1: Ajouter un élément à la liste
2: Retirer un élément de la liste
3: Afficher la liste
4: Vider la liste
5: Quitter""")

	choix = input("👉 Votre choix : ")	# Entrer utilisateur

	if choix == "1":	# Ajout d'un élément
		element = input("Entrez le nom d'un élément à ajouter à la liste de courses: ")
		liste.append(element)
		print(f"L'élément {element} a bien été ajouté à la liste.")

	elif choix == "3":	# Afficher le contenu de la liste de courses
		print("Voici le contenu de votre liste: ")
		if len(liste) == 0:
			print("Votre liste ne contient aucun élément.")
		else:
			for i in range(len(liste)):
				print(f"{i+1}. {liste[i]} ")

	elif choix == "2":	# Retirer un élément de la liste de courses
		sup_element = input("Entrez le nom d'un élément à retirer de la liste de courses : ")
		for i in range(len(liste)):
			if sup_element != liste[i]:
				continue
			elif sup_element == liste[i]:
				liste.remove(sup_element)
				print(f"L'élément {sup_element} a bien été supprimé de la liste.")
				break
			else:
				print(f"L'élément {sup_element} n'est pas dans la liste.")

	elif choix == "4":	# Vider la liste de courses
		liste.clear()
		print("La liste à été vidée de son contenu.")
		
	elif choix == "5":	# Quitter la liste de courses
		print("A bientôt !")
		break

