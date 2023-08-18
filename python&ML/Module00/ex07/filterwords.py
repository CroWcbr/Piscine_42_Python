from sys import argv
from string import punctuation

def main():
	if len(argv) != 3 or not isinstance(argv[1], str) or not argv[2].isdigit():
		print("Error input")
		return
	
	n = int(argv[2])
	str_without_punctuation = ''.join([char for char in argv[1] if char not in punctuation])
	result = [word for word in str_without_punctuation.split() if len(word) > n]
	print(result)

if __name__ == "__main__":
	main()
