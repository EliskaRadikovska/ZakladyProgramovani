matrix = [[-6, -8, -9, -20, -40], [-1, 5, 6, 100, -200], [-3, 6, 8, 60, -40], [-30, 4, 2, 4, -3], [-2, -4, -6, -7, -9]]

def matrix_sum(matrix, min_column, min_row, max_column, max_row):
    result = 0
    new_column = min_column
    while min_row <= max_row:
        while new_column <= max_column:
            result += matrix[min_row][new_column]
            new_column = new_column + 1
        new_column = min_column
        min_row = min_row + 1
    return result

m = len(matrix)
n = 1

max_result = 0
result_n = 0
result_column = 0
result_row = 0

min_column = 0
row = 0

while n <= m:
    row = 0
    while row <= m - n:
        new_column = min_column
        while new_column <= m - n: 
            result = matrix_sum(matrix, new_column, row, new_column + n - 1, row + n - 1)
            if result > max_result:
                max_result = result
                result_n = n
                result_column = new_column
                result_row = row
            new_column += 1
        row += 1
    n += 1

print(max_result)
print(result_n)
print(result_column)
print(result_row)







    


