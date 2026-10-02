
import numpy as np

def rmse(y_true, y_pred):
	difference = (np.subtract(y_true, y_pred))**2
	total = np.sum(difference)
	mse = total/y_true.size
	rmse_res = np.sqrt(mse)
	return round(rmse_res,3)
