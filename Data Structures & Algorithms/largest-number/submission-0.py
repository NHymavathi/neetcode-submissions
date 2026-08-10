from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not any(nums):
            return "0"

        def cmp(a, b):
            if a + b > b + a:
                return -1
            return 1

        return "".join(sorted(map(str, nums), key=cmp_to_key(cmp)))
        