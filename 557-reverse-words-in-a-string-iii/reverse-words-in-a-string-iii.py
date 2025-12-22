class Solution:
    def reverseWords(self, s: str) -> str:
        slist = []
        slist = s.split(" ")
        
        result = []
        for i in slist:
            result.append(i[::-1])
        
        new = ""
        new = " ".join(result)
        return new

