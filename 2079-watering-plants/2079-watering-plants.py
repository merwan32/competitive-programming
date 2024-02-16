class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        s = 0
        c = capacity
        for i in range(len(plants)):
            s += 1
            if c >= plants[i]:
                c -= plants[i]
            else:
                s += 2*i
                c = capacity - plants[i]
        return s

                

            