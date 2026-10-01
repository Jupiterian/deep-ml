import math
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	pivot1 = matrix[0][0]
	pivot2 = matrix[1][1]
	product = matrix[0][1] * matrix[1][0]

	a = 1
	b = - pivot1 - pivot2
	c = matrix[0][0] * matrix[1][1] - product
	eigenvalue1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
	eigenvalue2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
	return [eigenvalue1, eigenvalue2]