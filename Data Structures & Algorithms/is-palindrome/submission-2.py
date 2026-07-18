class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""

        for char in s.lower():
            if char.isalnum():
                clean += char
        return clean[::-1] == clean   