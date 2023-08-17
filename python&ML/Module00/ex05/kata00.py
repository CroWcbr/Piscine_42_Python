# Put this at the top of your kata00.py file
# The kata variable is always a tuple and can only be filled with integer.
kata = (19, 42, 21)

print(f"The {len(kata)} numbers are:", ", ".join(str(number) for number in kata))
