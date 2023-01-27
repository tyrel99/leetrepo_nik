class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        sett = set(list(words))
        res = []
        def checkword(word):
            for i in range(1, len(word)):
                lf = word[:i]
                rf = word[i:]
                
                if lf in sett and rf in sett:
                    return True
                if lf in sett and checkword(rf):
                    return True
                if rf in sett and checkword(lf):
                    return True

        for i in words:
            if checkword(i):
                res.append(i)
        return res
    
        
                
        