def anagram(s,t):
	flag=True
	if len(s)>len(t):
		a=s
		b=t
	else:
		a=t
		b=s
	for i in a.lower():
		if i not in b.lower() and i!=' ':
			flag= False
			break
	print(flag)

anagram("anagram", "nagaram")
anagram("Keep", "Peek")
anagram("Mother In Law", "Hitler Woman")
anagram("School Master", "The Classroom")
anagram("ASTRONOMERS", "NO MORE STARS")
anagram("Toss", "Shot")
anagram("joy", "enjoy")
anagram("Debit Card", "Bad Credit")
anagram("SiLeNt CAT", "LisTen AcT")
anagram("Dormitory", "Dirty Room")
