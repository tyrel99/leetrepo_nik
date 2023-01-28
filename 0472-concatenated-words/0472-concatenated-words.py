class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        sett = set(words)
        res = []
        dp = []
        mini = 10000
        
        def checkword(word):
            if word in dp:
                return True
            for i in range(mini,len(word)):
                pref = word[:i]
                suff = word[i:]
                
                if pref in sett:
                    if suff in sett or checkword(suff):
                        dp.append(word)
                        return True
            
            
        for i in words:
            mini = min(len(i), mini)
        for i in words:
            if checkword(i):
                res.append(i)
        return res
        
        