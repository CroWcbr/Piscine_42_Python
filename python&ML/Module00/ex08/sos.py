from sys import argv

morse_dict = {	'A':'.-',
				'B':'-...',
				'C':'-.-.',
				'D':'-..',
				'E':'.',
				'F':'..-.',
				'G':'--.',
				'H':'....',
				'I':'..',
				'J':'.---',
				'K':'-.-',
				'L':'.-..',
				'M':'--',
				'N':'-.',
				'O':'---',
				'P':'.--.',
				'Q':'--.-',
				'R':'.-.',
				'S':'...',
				'T':'-',
				'U':'..-',
				'V':'...-',
				'W':'.--',
				'X':'-..-',
				'Y':'-.--',
				'Z':'--..',
				'1':'.----',
				'2':'..---',
				'3':'...--',
				'4':'....-',
				'5':'.....',
				'6':'-....',
				'7':'--...',
				'8':'---..',
				'9':'----.',
				'0':'-----'}

def main():
	if (len(argv) == 1):
		return

	result = ' '.join(argv[1:]).upper().split()
	if not all(word.isalnum() for word in result):
		print("ERROR")
		return
	
	print(" / ".join(" ".join(morse_dict[char] for char in word) for word in result))

if __name__ == "__main__":
	main()
