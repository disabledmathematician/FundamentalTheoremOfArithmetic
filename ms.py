def CharlesSort(left, right, c):
	i, j = 0, 0
	fin = []
	while i < len(left) and j < len(right):
		if c(left[i], right[j]):
			fin.append(left[i])
			i += 1
		else:
			fin.append(right[j])
			j += 1
	while i < len(left):
		fin.append(left[i])
		i += 1
	while j < len(right):
		fin.append(right[j])
	return fin

def CharlesMerge(L):
	if len(L) < 2:
		return L[:]
	else:
		middle = len(L) // 2
		left = CharlesMerge(L[:middle])
		right = CharlesMerge(L[middle:])
		return CharlesSort(left, right, lambda x, y: x < y)
		
stmt = L = [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]; CharlesMerge(L) 
print("The unsorted list is {} and the sorted list is: ... \n".format(L))
print("{} ... \n using Merge Sort & Divide and Conquer".format(CharlesMerge(L)))
#from timeit import timeit
#print("It takes {} seconds to divide and conquer an 14 element list".format(timeit(setup=setup, stmt=stmt, number=10)))
		
		