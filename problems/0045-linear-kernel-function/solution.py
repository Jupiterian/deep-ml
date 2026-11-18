import numpy as np

def kernel_function(x1, x2):
    # Your code here
    dp = 0
    for i in range(0, len(x1)):
        dp += (x1[i] * x2[i])
    return dp
