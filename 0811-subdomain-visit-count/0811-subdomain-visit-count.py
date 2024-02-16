class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        mydict = {}
        for domain in cpdomains:
            n,d = domain.split()
            if d in mydict.keys():
                mydict[d] = mydict[d] + int(n)
            else: 
                mydict[d] =  int(n)
            
            
            
            first_point = d.index('.')
            d1 = d[first_point+1:]
            if d1 in mydict.keys():
                mydict[d1] = mydict[d1] + int(n)
            else: 
                mydict[d1] =  int(n)
            
            
            if '.' in d1:
                second_point = d1.index('.')
                d2 = d[first_point +second_point+2:]
                if d2 in mydict.keys():
                    mydict[d2] = mydict[d2] + int(n)
                else: 
                    mydict[d2] = int(n)
            
            
        result = []
        for d in mydict:
            result.append(str(mydict[d])+" "+d)
        return result