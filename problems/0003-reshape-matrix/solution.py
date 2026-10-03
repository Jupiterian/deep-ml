import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	reshaped_matrix = np.array(a)
	rowreshape = new_shape[0]
	colreshape = new_shape[1]
	if (rowreshape * colreshape == reshaped_matrix.size):
		reshaped_matrix = reshaped_matrix.reshape(rowreshape, colreshape)
		reshaped_matrix.tolist()
	else:
		reshaped_matrix = []
	return reshaped_matrix