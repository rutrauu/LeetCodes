import math
class Solution:
    def gcdOStrings(self, str1: str, str2: str) -> str:
        str1 == "ABC" 
        str2 == "ABCABC"

        _max = max(len(str1), len(str2))

        pointer = 0
        possible_prefix = ""
        prefix = ""

        while pointer < min(len(str1), len(str2)):
            if str1[pointer] == str2 [pointer]:
                possible_prefix += str1[pointer]
                pointer += 1
            else:
                break

            iterations = math.ceil(_max/len(possible_prefix))
            match1 = False
            match2 = False
            print(iterations)

            for i in range(1, iterations + 1):
                if possible_prefix*i == str1:
                    match1 = True
                if possible_prefix*i == str2:
                    match2 = True

            if (match1 and match2):
                prefix = possible_prefix


        return prefix