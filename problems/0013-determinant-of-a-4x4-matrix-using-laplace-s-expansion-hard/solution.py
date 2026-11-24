def determinant_4x4(matrix: list[list[int|float]]) -> float:
    # Your recursive implementation here
    
    r1 = matrix[0]
    r2 = matrix[1]
    det = 0
    for i in range(0,4):
        if i%2 == 0:
            sign = "+"
        else: 
            sign = "-"
        coeff = r1[i]
        # drop column and r1
        targetRow = 0
        targetcol = i
        result3x3 = [row[:] for row in matrix]        
        result3x3.pop(0)
        for row in result3x3:
            row.pop(i)

        # now apply formula
        minidet = (result3x3[0][0] * ((result3x3[1][1] * result3x3[2][2]) - (result3x3[1][2] * result3x3[2][1]))) - (result3x3[0][1] * ((result3x3[1][0] * result3x3[2][2]) - (result3x3[1][2] * result3x3[2][0]))) + (result3x3[0][2] * ((result3x3[1][0] * result3x3[2][1]) - (result3x3[1][1] * result3x3[2][0])))

        if sign == "+":
            det+=(coeff * minidet)
        else:
            det-=(coeff * minidet)

    return det        

        