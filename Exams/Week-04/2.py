def count(s):
	c=0
	for i in range(len(s)):
		if(s[i]=='1'):
			c+=1
	return c
def input(n):
	l=[]
	for i in range(0,n+1):
		a=format(i,'b')
		l.append(count(a))
	return l

print(input(15))
print(input(16))
print(input(1))
print(input(25))
print(input(5))
print(input(6))