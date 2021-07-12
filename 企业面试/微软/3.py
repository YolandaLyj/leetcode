def solution(S):
    # write your code in Python 3.6

    stack=[]
    for i in S:
        if len(stack)==0:
            stack.append(i)
        elif i+stack[-1] in ['AB','BA', 'CD', 'DC']:
            stack.pop(-1)
        else:
            stack.append(i)
    return ''.join(stack)

print(solution('ACACDBD'))
# print(solution('CBACD'))