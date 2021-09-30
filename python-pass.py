class Solution:
 
    @staticmethod
    def longest_palindromic(s: str) -> str:
        n = len(str)
        maxLength = 1
        start = 0
        longestStr = ''
        for i in range(n):
            for j in range(i, n):
                flag = 1
                for k in range(0, ((j - i) // 2) + 1):
                    if (str[i + k] != str[j - k]):
                        flag = 0
                if (flag != 0 and (j - i + 1) > maxLength):
                    start = i
                    maxLength = j - i + 1
        for i in range(start, start + maxLength):
          longestStr += str[i]
        return longestStr
str = input()
print(Solution.longest_palindromic(str))
