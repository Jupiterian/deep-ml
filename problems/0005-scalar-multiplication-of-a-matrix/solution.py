def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    # Your code here
    for row in matrix:
        for j in range(0, len(row)):
            row[j] = scalar * row[j]
    return matrix