class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dictionary = {}
        for i in range(len(nums)):
            if target-nums[i] in dictionary:
                return [dictionary[target-nums[i]], i]
            dictionary[nums[i]] = i

def main():
    nums = [2,7,11,15]
    target = 9
    print(Solution().twoSum(nums, target))

if __name__ == '__main__':
    main()