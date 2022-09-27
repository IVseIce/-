
l = [1,2,3,4,5]
for i in range(0,5):
    print(l[4-i], end = ", ")
print("")

j = 4
while j >= 0:
    print(l[j],end = ", ") 
    j -= 1
print("")

print(l[::-1])