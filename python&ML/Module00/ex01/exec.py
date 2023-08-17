from sys import argv

def main():
	if len(argv) < 2:
		return
	print(' '.join(argv[1:])[::-1].swapcase())
	# all_string = ' '.join(argv[1:])
	# reverse_string = all_string[::-1]
	# swap_string = reverse_string.swapcase()
	# print(swap_string)

if __name__ == "__main__":
	main()
