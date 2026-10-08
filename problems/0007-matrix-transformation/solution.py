import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	try:
		T_inverse = np.linalg.inv(T)
		S_inverse = np.linalg.inv(S)

	except:
		return -1

	transformed_matrix = T_inverse @ A @ S
	return transformed_matrix