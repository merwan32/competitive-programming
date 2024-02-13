class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        me2target = abs(target[0]) + abs(target[1])
        
        m = abs(ghosts[0][0]-target[0])+abs(ghosts[0][1]-target[1])
        for g in ghosts[1:] :
            m = min(abs(g[0]-target[0])+abs(g[1]-target[1]),m)
        
        return me2target < m