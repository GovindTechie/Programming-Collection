from typing import List

def spiral_copy(inputMatrix: List[List[int]]) -> List[int]:
    result = []
    if not inputMatrix or not inputMatrix[0]:
        return result
    
    top, bottom = 0, len(inputMatrix) - 1
    left, right = 0, len(inputMatrix[0]) - 1

    while top <= bottom and left <= right:
        for col in range(left, right+1):
            result.append(inputMatrix[top][col])
        top += 1

        for row in range(top, bottom+1):
            result.append(inputMatrix[row][right])
        right -= 1

        if top <= bottom:
            for col in range(right, left-1, -1):
                result.append(inputMatrix[bottom][col])
            bottom-=1
        
        if left <= right:
            for row in range(bottom, top-1, -1):
                result.append(inputMatrix[row][left])
            left+=1
        
    return result



inputMatrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(spiral_copy(inputMatrix))