def function(c):
	if c>='A' and c<='Z' or c>='a' and c<='z':
		return "Alphabet"
	else:
		return "Not a Alphabet"
n = raw_input()
print(function(n))
