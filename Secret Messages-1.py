letters = 'abcdefghijklmnopqrstuvwxyz'
table = {}
for i, j in zip(letters, letters[::-1]):
	table[ord(i)] = j
s = input().lower()
s = s.translate(table)
print(s)
