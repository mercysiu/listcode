# dung stack de chua dau ngoac mo
# gap ngoac dong rut stack dinh neu thoa thi cho qua khong thi tra ve False
# trong qua trinh duyet phan tu neu duyet toi ngoac dong ma stack trong thi False
# sau khi chay het phan tu trong s rao them dieu kien cuoi neu stack trong thi True
# stack khong trong tuc la co ngoac mo nhung khong co ngoac dong thì False
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

                    
    


  