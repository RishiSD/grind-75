class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        map: dict[int, int] = {}
        for x in range(len(nums)):
            if ((target - nums[x]) in map):
                return [map[target - nums[x]], x]
            map[nums[x]] = x
