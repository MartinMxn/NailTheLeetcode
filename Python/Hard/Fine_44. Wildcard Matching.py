class Solution:
    """
    backtrack
    if s[i] == p[j] or p[j] == '?'
        i++ j++
    elif s[i] != p[j] and p[j] == '*': 
        record the * idx
        record used_star_s_idx
    elif s[i] != p[j] * idx is still the initial one:
        return False
    else:
        set i to used_star_s_idx + 1
        set j to * idx + 1 
        then backtrack and continue
    
    after s reach the end, check whether the left chars in p are all *
    """
    def isMatch(self, s: str, p: str) -> bool:
        s_idx, p_idx = 0, 0
        pre_star_idx, used_star_s_idx = -1, 0
        while s_idx < len(s):
            if p_idx < len(p) and p[p_idx] in [s[s_idx], '?']:
                s_idx += 1
                p_idx += 1
            elif p_idx < len(p) and p[p_idx] == '*':
                pre_star_idx = p_idx
                used_star_s_idx = s_idx
                p_idx += 1
            elif pre_star_idx == -1:
                return False
            else:
                s_idx = used_star_s_idx + 1
                p_idx = pre_star_idx + 1
                used_star_s_idx = s_idx
                
        return all(x == '*' for x in p[p_idx:])
                
