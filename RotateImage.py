from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix)-1

        while l < r:
            for i in range(r-l):
                top, bottom = l, r

                topLeft = matrix[top][l+i]
                
                matrix[top][l+i] = matrix[bottom-i][l]
                matrix[bottom-i][l] = matrix [bottom][r-i]
                matrix[bottom][r-i] = matrix[top+i][r]
                matrix[top+i][r] = topLeft

            r-=1
            l+=1

        return matrix


matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
sol = Solution()
print(sol.rotate(matrix))