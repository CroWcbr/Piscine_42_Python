# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/13 16:15:10 by mli               #+#    #+#              #
#    Updated: 2021/11/21 16:03:01 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from sys import argv
from string import punctuation

def text_analyzer(*args) -> None:
	"""
	This function counts the number of upper characters, lower characters,
	punctuation and spaces in a given text.
	"""
	if len(args) > 1:
		print("AssertionError: more than one argument are provided")
		return
	elif len(args) == 0 or (len(args) == 1 and args[0] == "None"):
		print("What is the text to analyze?")
		print(">>", end = ' ')
		s = input()
	else:
		s = args[0]

	if not isinstance(s, str):
		print("AssertionError: argument is not a string")
		return

	UPPER = LOWER = PUNC = SPACE = LEN = 0
	for char in s:
		if char.islower():
			LOWER += 1
		elif char.isupper():
			UPPER += 1
		elif char in punctuation:
			PUNC += 1
		elif char.isspace():
			SPACE += 1
		LEN += 1
	print("The text contains", LEN, "character(s):")
	print("-", UPPER, "upper letter(s)")
	print("-", LOWER, "lower letter(s)")
	print("-", PUNC, "punctuation mark(s)")
	print("-", SPACE, "space(s)")

if __name__ == "__main__":
	if (len(argv) == 1):
		text_analyzer()
	else:
		text_analyzer(*argv[1:])
