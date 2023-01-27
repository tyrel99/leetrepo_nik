class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        sett = set(words)
        res = []
        dp = []
        mini = 10000
        def checkword(word):
            if word in dp:
                return True
            for i in range(mini, len(word)):
                lf = word[:i]
                rf = word[i:]
                
                if lf in sett:
                    if rf in sett or checkword(rf):
                        dp.append(word)
                        return True
        
        for i in words:
            mini = min(len(i), mini)
        for i in words:
            if checkword(i) == True:
                res.append(i)
        return res
    
        
                
        