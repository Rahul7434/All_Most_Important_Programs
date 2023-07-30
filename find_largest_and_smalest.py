l=[10,15,3,4,12]
lar=l[0]
small=l[0]
for i in l:
    if i > lar:
        lar=i
    elif i < small:
        small=i

print("largesr=",lar)
print("smallest=",small)

           

