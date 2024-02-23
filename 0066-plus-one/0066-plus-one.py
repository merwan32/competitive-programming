class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        index = len(digits) -1       
        while True:
            if digits[index] != 9:
                digits[index] += 1
                break
            elif index >= 0:
                digits[index] = 0
                if index == 0:
                    digits = [1] + digits
                    break
                else:
                    index -= 1
            
                
        return digits
                