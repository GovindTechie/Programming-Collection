'''Parking Lot Fullness:
Problem: Given a parking lot represented as a matrix with R rows and C
columns, where each element is either 0 (empty) or 1 (full), find the index
of the row with the most full parking spaces.
Input:
▪ Two integers R and C representing the number of rows and
columns
▪ A matrix of size R x C with elements 0 or 1
Output:
▪ An integer representing the index of the row with the most full
parking spaces
Example:
▪ Input: R = 3, C = 3, Matrix = [[1, 0, 1], [1, 1, 1], [0, 0, 0]]
▪ Output: 1 (second row has the most full spaces) 
'''


class Solution():
    def ParkingLotFullness(self, R, C, matrix):
        max_count = -1
        row_index = -1

        for i in range(R):
            count = sum(matrix[i])
            if count > max_count:
                max_count = count
                row_index = i

        return row_index
        
        
s1 = Solution()
R, C = map(int, input("Enter number of row and column ").split())
matrix = [list(map(int, input().split()))for _ in range(R)]
print(f"The matrix is :")
for row in matrix:
    print(*row)
print(f"The row index that has most full space : {s1.ParkingLotFullness(R, C, matrix)}")
