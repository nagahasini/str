def is_same(a,b):
    if (a=='(' and b==')') or (a=='[' and b==']') or (a=='{' and b=='}') :
        return True
    else:
        return False



def balanced_paranthesis(expr):
    s=[]
    for x in expr:
        if x in ('(','{','['):
            s.append(x)
        else:
            if not s:
                return False
            elif is_same(x,)
