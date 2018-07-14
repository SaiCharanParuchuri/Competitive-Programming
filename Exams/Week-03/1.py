def binary(n):
	l=[0,0,0,0,0,0,0,0]
	i=7
	while n!=0:
		r=n%2
		n=n//2
		l[i]=l[i]+r
		i-=1
		# print(l)
	return l

def distance(a,b):
	m=binary(a)
	n=binary(b)
	c=0
	if len(m)<len(n):
		s1=len(m)
		s2=len(n)
	else:
		s1=len(n)
		s2=len(m)
	for i in range(0,s1):
		if m[i]!=n[i]:
			c+=1
	c=c+(s2-s1)
	return c

print(distance(25,30))
print(distance(1,4))
print(distance(25,30))
print(distance(100,250))
print(distance(1,30))
print(distance(0,255))