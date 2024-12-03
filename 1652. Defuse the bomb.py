class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        new_array = []
        elements_distances = range(1, k + 1) if k >= 0 else range(k, 0)
        mod = len(code)
        for index, element in enumerate(code):
            new_element = sum([code[(index + distance) % mod ] for distance in elements_distances])
            new_array.append(new_element)
        return new_array    