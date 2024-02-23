class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = []
        for i in range(n):
            arr.append(i+1)
          
        index = 0
        while len(arr)!=1:
            
            index = (index + k -1 )%len(arr)
            arr.pop(index)
            
        return arr[0]
            