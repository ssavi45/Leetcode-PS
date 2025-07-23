# Given a string s consisting of words and spaces, return the length of the last word in the string.
#A word is a maximal substring consisting of non-space characters only.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        end = len(s) - 1

        while s[end] == ' ':
            end -= 1

        start = end
        while start >= 0 and s[start] != ' ':
            start -= 1

        return end - start

sol = Solution()
print(sol.lengthOfLastWord('hello world'))
print(sol.lengthOfLastWord('fly   me   to the    moon '))
print(sol.lengthOfLastWord('luffy is still a joyboy'))
