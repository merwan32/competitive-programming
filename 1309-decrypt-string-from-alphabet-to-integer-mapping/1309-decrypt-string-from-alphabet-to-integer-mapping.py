class Solution:
    def freqAlphabets(self, s: str) -> str:
        string = ''
        i = len(s)-1
        while i >= 0:
            if s[i] == '#':
                string =  chr(int(s[i-2:i])+96) + string
                i =i - 3
            else:
                string =  chr(int(s[i])+96) + string
                i = i -1
        return string
