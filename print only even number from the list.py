size=int(input("enter a size"))
l=[]
for i in range(size):
    new_user=int(input("enter a element"))
    l.append(new_user)
print(l)
#even number
for j in l:
    if(j%2==0):
        print(j)


