while True:
	print("Choose character:")
	print("Blauw" , "Foxtrot", sep='\n')
	chooseclass = input()
	if (chooseclass =="Foxtrot"):
		name = ("Foxtrot")
		power = ('Fire')
		speed = ('200')
		weapon = ('bow, dagger')
		inventory = ('A quiver[with 20 arrows]')
		armor = ("a cloak with a leather jacket over it")
	if (chooseclass == "Foxtrot"):
		print("Name: "+ name, "Power: "+ power, "Speed: "+ speed, "Weapon: "+ weapon, "Inventory: "+ inventory, "Armor: "+ armor, sep='\n')
		if input("Back? (Y/N):") == "Y": continue
		elif "N": break
			

	if (chooseclass =="Blauw"):
		name = ("Blauw")
		power = ('Blink')
		speed = ('100')
		weapon = ('two knives')
		inventory = ('a block of cheese')
		armor = ("leather")
	if (chooseclass == "Blauw"):
		print("Name: "+ name, "Power: "+ power, "Speed: "+ speed, "Weapon: "+ weapon, "Inventory: "+ inventory, "Armor: "+ armor, sep='\n')
		if input("Back? (Y/N):") == "Y": continue
		elif "N": break