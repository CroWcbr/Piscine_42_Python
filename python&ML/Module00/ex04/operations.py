from sys import argv

def main():
	if len(argv) != 3:
		if len(argv) == 2:
			print("AssertionError: only one argument, but needed two arguments")
		elif len(argv) != 3:
			print("AssertionError: more than two arguments are provided")
		return

	try:
		A = int(argv[1])
		B = int(argv[2])
	except ValueError:
		print("AssertionError: one of argument is not an integer")
		return

	print("Sum:\t\t", A + B)
	print("Difference:\t", A - B)
	print("Product:\t", A * B)
	print("Quotient:\t", A / B if B != 0 else "ERROR (division by zero)")
	print("Remainder:\t", A % B if B != 0 else "ERROR (modulo by zero)")


if __name__ == "__main__":
	main()
