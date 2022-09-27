def solution(s):
    if len(s)==0:
        return 0
    s+=' '
    num=1
    temp=1
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            temp+=1
        else:
            num=max(temp,num)
            temp=1
    return num

s = input()
print(solution(s))

