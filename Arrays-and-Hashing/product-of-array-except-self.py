class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        for i in range(0, len(nums)):
            output = nums[:i] + nums[i+1:]
            mult = 1
            for n in output:
                mult = mult * n
            result.append(mult)
        return result

