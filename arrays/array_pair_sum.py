def pair_sum(array, k):
	array.sort()
	i = 0
	j = len(array) - 1
	tuples = []

	while i < j:
		total = array[i] + array[j]
		if total > k:
			j -= 1
		elif total < k:
			i += 1
		elif total == k:
			tuples.append((array[i], array[j]))
			i += 1
	return tuples
