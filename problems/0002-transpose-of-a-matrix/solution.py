def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    T = []
    for i in range(0, len(a[0])):
        col = []
        for row in a:
            element = row[i]
            col.append(element)

        T.append(col)
    return T