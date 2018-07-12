mc={
'A' :".-",
'B' :"-...",
'C' :"-.-.",
'D' :"-..",
'E' :".",
'F' :"..-.",
'G' :"--.",
'H' :"....",
'I' :"..",
'J' :".---",
'K' :"-.-",
'L' :".-..",
'M' :"--",	
'N' :"-.",
'O' :"---",
'P' :".--.",
'Q' :"--.-",
'R' :".-.",
'S' :"...",
'T' :"-",
'U' :"..-",
'V' :"...-",
'W' :".--",
'X' :"-..-",
'Y' :"-.--",
'Z' :"--.."
}

def morse(l):
	nl=[]
	c=0
	for i in l:
		s=""
		i=i.upper()
		for j in range(len(i)):
			s+=mc[i[j]]
		# print(s)
		if(s not in nl):
			c=c+1
		nl.append(s)
	print(c)
	
morse(["gin", "zen", "gig", "msg"])
morse(["a", "z", "g", "m"])
morse(["bhi", "vsv", "sgh", "vbi"])
morse(["a", "b", "c", "d"])
morse(["hig", "sip", "pot"]  )