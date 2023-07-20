def matrixmul(matrix,m):
      
      matrix=[[i*2 for i in row]for row in matrix]
      return matrix

matrix=[]
while True:
        row_input = input()
        if row_input.lower() == 'done':
            break
        row = [int(num) for num in row_input.split()]  # Convert the input string to a list of integers
        matrix.append(row)
m=int(input())
print(matrixmul(matrix,m))

