import numpy as np

def accuracy_score(y_true, y_pred):
    # Your code here
    '''
    total = len(y_true)
    acc = 0
    for i in range(0, len(y_true)):
        if y_true[i] == y_pred[i]:
            acc+=1

    accuracy = acc/total
    return accuracy
    '''
    return np.mean(y_true == y_pred)