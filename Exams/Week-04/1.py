def count(s):
	c=0
	cm=0
	for i in range(len(s)):
		if(s[i]=='1'):
			c+=1
		else:
			if(c>cm):
				cm=c
				c=0
	return cm
def input(n):
	a=format(n,'b')
	print(a)
	print(count(a))

input(0)
input(55)
input(-5)
input(12345)
input(6)
input(256)