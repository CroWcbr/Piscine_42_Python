from random import randint as rand


def main():
	print("\
This is an interactive guessing game!\
You have to enter a number between 1 and 99 to find out the secret number.\
Type 'exit' to end the game.\
Good luck!\n")
	
	secret = rand(1, 99)
	count = 0
	while True:
		s = input("What's your guess between 1 and 99?\n>> ")
		if s == "exit":
			print("Goodbye!")
			return
		
		if not s.isdigit():
			print("Wrong input!")
			continue
		else:
			s = int(s)
			if s < 1 or s > 99:
				print("Wrong input!")
				continue

		count += 1
		if secret > s:
			print("Too low!")
		elif secret < s:
			print("Too high!")
		else:
			break

	if (secret == 42):
		print("The answer to the ultimate question of life, the universe and everything is 42.")
	if (count > 1):
		print("Nice, indeed it was", secret, "and you won in", count, "attempts")
	else:
		print("Wow, first try ! Congrats")

if __name__ == "__main__":
	main()
