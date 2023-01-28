class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        sett = set(words)
        res = []
        mini = 10000
        
        def checkword(word):
            for i in range(mini,len(word)):
                pref = word[:i]
                suff = word[i:]
                
                if pref in sett and suff in sett:
                    return True
                if pref in sett and checkword(suff):
                    return True
            
            
        for i in words:
            mini = min(len(i), mini)
        for i in words:
            if checkword(i):
                res.append(i)
        return res
        
        