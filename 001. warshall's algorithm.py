# Warshall's algorithm
def warshall(matrix):
    '''
    matrix: the matrix to find the transitive closure using the Warshall's algorithm
    length: the length of the matrix for the range of computation in loops
    i, j, k for loops and raw-column operations
    returns the success message because no need to return the matrix itself
    as it is printed in the function
    '''
##============================================================================    
    length = len(matrix)
    for k in range(length):
        for i in range(length):
            for j in range(length):
                matrix[i][j] = matrix[i][j] or (matrix[i][k] and matrix[k][j])
        for i in range(row):
            for j in range(column):
                m = str(matrix[i][j])
                print(m, end = ' ' * (5 - len(m)))
            print()
        print('=' * 50)
##============================================================================

    success = 'End of the transitive closure computation.'
    return success

# entering matrix size NxN
print('=' * 50)
n = int(input('Enter the NxN matrix size (N): '))
row = column = n

# initializing empty matrix
matrix = []
print('=' * 50)
print('Enter the entries (1s and 0s) rowwise: ')

# entering the matrix elements, i.e. 1s and 0s

# for loop for row entries
for i in range(row):
    a =[]
    # for loop for column entries
    for j in range(column):
        a.append(int(input('m[{0}][{1}] = '.format(i+1, j+1))))
    matrix.append(a)
        
print('=' * 15, 'Original Relation.', '=' * 15,)
# printing the matrix
for i in range(row):
    for j in range(column):
        m = str(matrix[i][j])
        print(m, end = ' ' * (5 - len(m)))
    print()
print('=' * 5, 'Computation of the transitive closure.', '=' * 5)

# calling the function
print(warshall(matrix))
print('=' * 50)

## written by Khasan Rashidov
