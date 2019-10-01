p_list = list(input())
arr = []
for i in p_list:
	if i in ["(","[","{"]:
		arr.append(i)
	elif i in [")","]","}"]:
		if arr and (ord(i) - ord(arr[-1])) in [1,2]:
			arr.pop()
		else:
			print("Invalid")
			break
else:
	print("Valid")
