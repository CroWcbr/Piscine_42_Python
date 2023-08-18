cookbook = {
	"Sandwich"	:	{	"ingredients"	:	{"ham", "bread", "cheese", "tomatoes"},
						"meal"			:	"lunch",
						"prep_time"		:	10},
	"Cake"		:	{	"ingredients"	:	{"flour", "sugar", "eggs"},
						"meal"			:	"dessert",
						"prep_time"		:	60},
	"Salad"		:	{	"ingredients"	:	{"avocado", "arugula", "tomatoes", "spinach"},
						"meal"			:	"lunch",
						"prep_time"		:	15},
}

def add_recipe():
	name = input(">>> Enter a name: ").strip()
	ingredients = []
	print(">>> Enter ingredients:")
	while True:
		s = input().strip()
		if s == "":
			break
		if s in ingredients:
			print("The ingredient don't added! It is duplicated!!!")
		else:
			ingredients.append(s)
	meal = input(">>> Enter a meal type: ").strip()
	while True:
		prep_time = input(">>> Enter a preparation time: ").strip()
		if prep_time.isdigit():
			prep_time = int(prep_time)
			break
		else:
			print("Wrong preparation time!")

	if name in cookbook:
		print("Recipe {} rewrite".format(name))
	else:
		print("Recipe {} added".format(name))
	cookbook[name] = {	"ingredients": ingredients,
						"meal": meal,
						"prep_time": prep_time}
	

def delete_recipe(name):
	if len(name) == 0:
		return
	cookbook.pop(name)
	print("Recipe {} deleted".format(name))

def print_recipe(name):
	if len(name) == 0:
		return
	print("Recipe for", name)
	print("\tIngredientes list: {}".format(cookbook[name]["ingredients"]))
	print("\tTo be eaten for {}.".format(cookbook[name]["meal"]))
	print("\tTakes {} minutes of cooking.".format(cookbook[name]["prep_time"]))

def print_all():
	print("Print the cookbook:")
	if len(list(cookbook)) == 0:
		print("Empty!")
	else:
		for recipe_name in cookbook:
			print_recipe(recipe_name)

def input_recipe_name(t):
	while True:
		if t == 3:
			if len(list(cookbook)) == 0:
				print("Cookbook is empty : any cannot be printed")
				return ""
			print("Please enter a recipe name to get its details:\n>>", end = ' ')
		else:
			if len(list(cookbook)) == 0:
				print("Cookbook is empty : any cannot be deleted")
				return ""
			print("Please enter a recipe name to delete its recipe:\n>>", end = ' ')

		s = input()
		if s in cookbook:
			return s
		else:
			print("Wrong recipe name. Input:")
			for recipe_name in cookbook:
				print("\t", recipe_name)

def main():
	print("Welcome to the Python Cookbook !")
	while True:
		print("\nList of available option:")
		print("\t1: Add a recipe")
		print("\t2: Delete a recipe")
		print("\t3: Print a recipe")
		print("\t4: Print the cookbook")
		print("\t5: Quit")
		print("")

		print("Please select an option:\n>>", end = ' ')
		s = input()
		if s.isdigit():
			opt = int(s)
			if opt == 1:
				add_recipe()
			elif opt == 2:
				delete_recipe(input_recipe_name(opt))
			elif opt == 3:
				print_recipe(input_recipe_name(opt))
			elif opt == 4:
				print_all()
			elif opt == 5:
				break
			else:
				print("Sorry, this option does not exist.")
		else:
			opt = s
	print("Cookbook closed. Goodbye !")

if __name__ == "__main__":
	main()
