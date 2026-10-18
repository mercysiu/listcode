class Solution(object):
    def isValid(self, s):
        if not s:
            return False
        stack = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            else:
                if not stack:
                    return False
                else:
                    p_o = stack.pop()
                    if i == ')':
                        if p_o != '(':
                            return False
                    if i == ']':
                        if p_o != '[':
                            return False
                    if i == '}':
                        if p_o != '{':
                            return False
        if not stack:
            return True
        else:
            return False

                    
    


  