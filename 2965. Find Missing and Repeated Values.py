class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        size = len(grid)**2
        found_numbers = [0 for i in range(size)]
        for row in grid:
            for elem in row:
                found_numbers[elem - 1] += 1
        a = 0
        b = 0
        for index, found_number in enumerate(found_numbers):
            if found_number == 0:
                b = index + 1
            if found_number == 2:
                a = index + 1
        return [a, b]            
