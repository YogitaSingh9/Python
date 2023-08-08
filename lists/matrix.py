list = [[1, 2, 63], [2, 4, 5], [6, 7, 5]]
print("The original list is : " + str(list))
res = []
for i in list:
	res.append([[ele, i[-1]] for ele in i[:-1]])
print ("The list after pairing is : " + str(res))
