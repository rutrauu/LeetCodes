from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        water = [0]*n

        high = 0

        for i in range (0, n):
            if height[i] > high:
                high = height[i]

            if height[i] < high:
                water[i] += high - height[i]

        high = 0

        for i in range(n-1, 0, -1):
            if height[i] > high:
                high = height[i]

            diff = high - height[i]

            if diff < water[i]:
                water[i] = diff

        return sum(water)
    
sol = Solution()

height = [4,2,0,3,2,5]
resultado = sol.trap(height)

# Exibindo o resultado
print(f"A quantidade de água retida é: {resultado}")
