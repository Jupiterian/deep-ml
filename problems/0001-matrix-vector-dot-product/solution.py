def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	if len(a[0]) != len(b):
		return -1
	else:
		product = []
		sum = 0
		for row in a:
			sum = 0
			for i in range(0,len(row)):
				sum = sum + (row[i] * b[i])
			product.append(sum)
		return product
