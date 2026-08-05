class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""

        for ch in s:
            if ch.isalnum():
                cleaned += ch.lower()

        start, end = 0, len(cleaned) - 1

        while start < end:
            if cleaned[start] != cleaned[end]:
                return False
            start += 1
            end -= 1

        return True

        return True
        