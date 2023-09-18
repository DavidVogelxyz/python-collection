class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # mapping value : index  # this is python, so this object (js/ts) or map is called a dictionary

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return
