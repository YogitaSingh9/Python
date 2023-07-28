# Python program to multiply all values in the
# list using traversal


def multiplyList(list):
	r = 1
	for x in list:
		r = r* x
	return r
l1 = [1, 2, 3]
l2 = [3, 2, 4]
print(multiplyList(l1))
print(multiplyList(l2))
