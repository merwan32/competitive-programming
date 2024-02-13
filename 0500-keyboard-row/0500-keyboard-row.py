class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        raw1 = "qwertyuiop"
        raw2 = "asdfghjkl"
        raw3 = "zxcvbnm"
        
        result = []
        for w_ in words:
            w = w_.lower()
            check = True

            if w[0] in raw1:
                for c in w[1:]:
                    if c not in raw1:
                        check = False
                        break
            if w[0] in raw2:
                for c in w[1:]:
                    if c not in raw2:
                        check = False
                        break
            if w[0] in raw3:
                for c in w[1:]:
                    if c not in raw3:
                        check = False
                        break
            if check :
                result.append(w_)
        return result
                
                
                