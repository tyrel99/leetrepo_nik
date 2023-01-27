class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        sett = set(words)
        res = []
        def checkword(word):
            for i in range(len(word)):
                lf = word[:i]
                rf = word[i:]
                
                if lf in sett:
                    if rf in sett or checkword(rf):
                        return True
        
        for i in words:
            if checkword(i) == True:
                res.append(i)
        return res
    
        
                
        