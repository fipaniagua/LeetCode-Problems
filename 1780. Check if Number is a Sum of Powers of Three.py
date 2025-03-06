def can_convert_to_power(n):
    
    toConvert = n
    while toConvert > 0:
      rest = toConvert % 3
      toConvert //= 3 
      if rest == 2:
        return False
    return True




class Solution(object):
    def checkPowersOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return can_convert_to_power(n)