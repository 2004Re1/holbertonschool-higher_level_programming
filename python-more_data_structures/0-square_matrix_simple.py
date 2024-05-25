#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
  new_Matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
  row = len(matrix)
  for i in range(row):
    for j in range(len(matrix[0])):
      new_Matrix[i][j] = matrix[i][j]**2
  return new_Matrix
