
def sort(left, right, compare):
	i, j = 0, 0
	sorted = []
	while i < len(left) and j < len(right):
		if compare(left[i], right[j]):
			sorted.append(left[i])
			i += 1
		else:
			sorted.append(right[j])
			j += 1
	while i < len(left):
		sorted.append(left[i])
		i += 1
	while j < len(right):
		sorted.append(right[j])
		j += 1
	return sorted
def merge(L):
	if len(L) < 2:
		return L[:]
	else:
		middle = len(L) // 2
		left = merge(L[:middle])
		right = merge(L[middle:])
		return sort(left, right, lambda x, y: x > y)
		
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(merge(L))