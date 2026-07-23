class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(s):
            return False

        char_list_s = {}

        for i in s:
            if i not in char_list_s:
                char_list_s[i] = 1
            else:
                char_list_s[i] += 1

        char_list_t = {}

        for i in t:
            if i not in char_list_t:
                char_list_t[i] = 1
            else:
                char_list_t[i] += 1

        if len(char_list_s) != len(char_list_t):
            return False

        for k,v in char_list_s.items():
            if k not in char_list_t:
                return False
            elif char_list_t[k] != v:
                return False

        for k,v in char_list_t.items():
            if k not in char_list_s:
                return False
            elif char_list_s[k] != v:
                return False
        
        return True
            
        