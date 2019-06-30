class Solution:
    def decodeString(self, s: str) -> str:
        stack, cur_num, cur_string = [], 0, ""
        
        for c in s:
            'num, letter, [, ], '
            if c == '[':    #2a[3b[4c]]
                stack.append(cur_string)
                stack.append(cur_num)
                cur_string = ''
                cur_num = 0
            elif c == ']':
                pre_num = stack.pop()
                pre_string = stack.pop()
                cur_string = pre_string + pre_num * cur_string
            elif c.isdigit():
                cur_num = cur_num * 10 + int(c) # 23[ab]
            else:   # letter
                cur_string += c
        
        return cur_string
