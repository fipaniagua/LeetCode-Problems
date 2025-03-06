class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        lesser_nums = []
        greater_nums = []
        equal_nums = []
        for num in nums:
            if num < pivot:
                lesser_nums.append(num)
            elif num == pivot:
                equal_nums.append(num)
            elif num > pivot:
                greater_nums.append(num)
        return lesser_nums + equal_nums + greater_nums            
