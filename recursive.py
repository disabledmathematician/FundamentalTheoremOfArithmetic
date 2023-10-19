def merge(left, right, c):
		r = []
		i, j = 0, 0
		print(left, right)
		while i < len(left) and j < len(right):
			if c(left[i], right[i]):
				r.append(left[i])
				i += 1
			else:
				r.append(right[j])
				j += 1
		while i < len(left):
			r.append(left[i])
			i += 1
		while j < len(right):
			r.append(right[j])
			j += 1
		print("r: {}".format(r))
		return r

def DivideAndConquer(L):
	if len(L) < 2:
		return L[:]
	else:
		middle = len(L) // 2
		l = DivideAndConquer(L[:middle])
		r = DivideAndConquer(L[middle:])
		return merge(l, r, lambda x, y: x < y)
		
#L = ["apples", "pears", "peaches", "bananas", "milk", "bread", "butter", "eggs", "cheese"]
L = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
r = DivideAndConquer(L)
print("Final Result: {}".format(r))