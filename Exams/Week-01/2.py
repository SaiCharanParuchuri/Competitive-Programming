def room(keys):
	n = len(keys)
	rooms=[0]*n
	rooms[0]=1
	for i in range(len(keys)):
		if(rooms[i] == 1):
			for j in keys[i]:
				if j < len(rooms):
					rooms[j] = 1
	flag = True
	for i in rooms:		
		if i == 0:
			flag = False
			break
	
	print(flag)
		
room([[1], [0,2], [3]])
room([[1,3], [3,0,1], [2], [0]])
room([[1,2,3], [0], [0], [0]])
room([[1], [0,2,4], [1,3,4], [2], [1,2]])
room([[1], [2,3], [1,2], [4], [1], [5]])
room([[1], [2], [3], [4], [2]])
room([[1], [1,3], [2], [2,4,6], [], [1,2,3], [1]])