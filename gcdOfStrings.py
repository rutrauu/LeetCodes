import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        tamanho_gcd = math.gcd(len(str1), len(str2))
        return str1[:tamanho_gcd]

# Exemplo de uso
sol = Solution()
print(sol.gcdOfStrings("ABC", "ABCABC"))
