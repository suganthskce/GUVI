def function(c):
	if c=='a' or c=='A' or c=='e' or c=='E' or c=='i' or c=='I' or c=='o' or c=='O' or c=='u' or c=='U':
		return "Vowel"
	elif c>='A' and c<='Z' or c>='a' and c<='z':
		return "Consonant"
	else:
		return 0
n = raw_input()
print(function(n))
