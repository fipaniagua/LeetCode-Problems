class Solution(object):
    def canChange(self, start, target):
        """
        :type start: str
        :type target: str
        :rtype: bool
        """
        left_index = 0
        target_index = 0
        len_target = len(target)
        len_start = len(start)
        target_letters = len(target.replace("_", ""))
        letter_counters = 0
        if len(start.replace("_", "")) != target_letters:
            return False

        while target_index < len_target:
            
            current_target = target[target_index]
            current_start = start[left_index]

            if current_start == current_target:
                target_index += 1
                left_index += 1
                if current_start != "_":
                    letter_counters += 1
                if current_target == "L" and target_index > left_index:
                    return False

                if letter_counters == target_letters:
                    return True

            elif current_target == "_":
                if current_start == "L" and target_index >= left_index:
                    return False
                target_index += 1

            elif current_target == "L":
                if current_start == "R":
                    return False
                left_index += 1

            elif current_target == "R":
                left_index += 1
                if left_index > target_index:
                    return False        

            if left_index >= len_start:
                return False    
        
        return True