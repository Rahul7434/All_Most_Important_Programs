l1=[1,2,3,4,4,2,5,6]
l2=[]

for i in l1:
    if i not in l2:
        l2.append(i)

print(l2)
