def output(matrix, l):
    output = matrix.copy()
    for k in range(l):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if output[i][j] and output[i][k] and output[k][j]:
                    if output[i][j] > output[i][k] + output[k][j]:
                        output[i][j] = output[i][k] + output[k][j]
                elif output[i][k] and output[k][j]:
                    output[i][j] = output[i][k] + output[k][j]
    for i in range(len(matrix)): 
        output[i][i] = 0
    return output