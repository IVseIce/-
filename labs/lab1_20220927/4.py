
s1 = input()
s2 = ''
for i in range(0,len(s1)-1):
    if s1[i] != ' ':
        s2 += s1[i]
print(s2)