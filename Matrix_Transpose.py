def transpose(matrix):
    return list(map(list, zip(*matrix)))

rows = int(input("Enter the number of rows in the matrix: "))
matrix = []
for _ in range(rows):
    row = list(map(int, input(f"Enter the values for row {_ + 1}, separated by spaces: ").split()))
    matrix.append(row)

print("Original matrix:")
for row in matrix:
    print(row)
transposed_matrix = transpose(matrix)
print("Transposed matrix:")
for row in transposed_matrix:
    print(row)
