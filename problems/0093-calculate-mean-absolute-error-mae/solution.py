import numpy as np

def mae(y_true, y_pred):
    """
    Calculate Mean Absolute Error between two arrays.

    Parameters:
        y_true (numpy.ndarray): Array of true values
        y_pred (numpy.ndarray): Array of predicted values

    Returns:
        float: Mean Absolute Error
    """
    # Your code here
    mae1 = 0
    y_true = y_true.flatten()
    y_pred = y_pred.flatten()
    for i in range(0,len(y_true)):
        mae1 = mae1 + abs(y_pred[i] - y_true[i])
    mae1 = mae1/len(y_true)
    return mae1