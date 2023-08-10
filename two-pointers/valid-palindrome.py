class Solution:
    def isPalindrome(self, s: str) -> bool:
        # lowercase the string and remove all non-alphabetical characters
        s = [char.lower() for char in s if char.isalnum()]
        # if string is equal to the reverse of the string
        return s == s[::-1]
