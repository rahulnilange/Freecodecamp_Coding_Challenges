

"""
Matrix Rotate

Given a matrix (an array of arrays), rotate the matrix 90 
degrees clockwise and return it. For instance, given [[1, 2], [3, 4]]
You should return [[3, 1], [4, 2]]

rotate([[1]]) should return [[1]]
rotate([[1, 2], [3, 4]]) should return [[3, 1], [4, 2]]
rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) should return 
[[7, 4, 1], [8, 5, 2], [9, 6, 3]]
rotate([[0, 1, 0], [1, 0, 1], [0, 0, 0]]) should return
[[0, 1, 0], [0, 0, 1], [0, 1, 0]]

"""

def rotate(matrix):
    # *matrix unpacks lists inside matrix
    result = [list(item)[::-1] for item in zip(*matrix)]
    return result
