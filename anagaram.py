def solution(s,t):
    """
    This fucntion verify if a string s, t is anagram of each other.
    This will return true for anagaram, else false.
    """
    if len(s) != len(t):
        return False
    
    hashS, hashT = {}, {}

    for i in range(len(s)):
        hashS[s[i]] = 1, hashS.get(s[i], 0)
        hashT[t[i]] = 1, hashT.get(t[i], 0)

    for ch in hashT:
        if hashT[ch] != hashS.get(ch, 0):
            return False
        
    return True, hashS, hashT
        

s = 'DeepakBari'
t = 'DeepkaariB'
print(solution(s, t))
