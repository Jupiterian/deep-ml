import numpy as np

def cosine_similarity(v1, v2):
    """
    Calculate the cosine_similarity of two vectors.
    Args:
        vec1 (numpy.ndarray): 1D array representing the first vector.
        vec2 (numpy.ndarray): 1D array representing the second vector.
    Returns:
        The cosine_similarity of the two vectors.
    """
    # Implement your code here
    ## cos(theta) = v1 dot v2 // ||v1||*||v2||
    ## derivation: using projections - taking the magnitude - and then doing algebra
    cos = np.dot(v1, v2)/(np.sqrt(np.dot(v1, v1)) * np.sqrt(np.dot(v2, v2)))
    return cos