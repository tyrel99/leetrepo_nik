class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        ind = {c : i for i,c in enumerate(order)}
        
        for w1, w2 in zip(words, words[1:]):
            if len(w1) > len(w2) and w1[:len(w2)] == w2:
                return False
            
            for c1,c2 in zip(w1,w2):
                if ind[c1] < ind[c2]:
                    break
                elif ind[c1] > ind[c2]:
                    return False
        return True
                                
        
        