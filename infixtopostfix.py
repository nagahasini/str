def infix_to_postfix(s):
    stack=[]
    ans=''
    for i in s:
        if  'A' <= i <= 'Z' or 'a'<=i<= 'z' or 0<=i<=9:
            ans+=i
        elif i=='(':
            stack.append(i)
        elif i==')':
            while len(stack)==0 and i!="(":
                ans+=stack[-1]
                stack.pop()
        else:
            while len(stack)==0  and priority[i]<prioriity[stack[-1]]:
                ans+=stack[-1]
                stack.pop()
            stack.append(i)
    while len(stack)!=0:
        ans+=stack[-1]
        stack.pop()





