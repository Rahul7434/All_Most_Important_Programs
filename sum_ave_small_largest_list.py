l=[10,23,45,12,77]
max=l[0]
min=l[0]
sum=0
c=0
for i in l:
    sum=sum+i
    c=c+1
    if i > max:
        max=i
    elif i < min:
        min=i

avg=sum/c

print("All Elements Sum =",sum)
print("Average =",avg)
print("Largest =",max)
print("Smallest =",min)

