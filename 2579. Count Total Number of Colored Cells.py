def getColored(n):
    if n == 1:
        return 1
    return (n-1)*4 + getColored(n-1)

class Solution(object):
    def coloredCells(self, n):
        """
        :type n: int
        :rtype: int
        1 1 +4
        2 5 +8 
        3 13 +12
        4 25 
        """
        return getColored(n)