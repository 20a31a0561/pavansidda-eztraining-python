'''
size=int(input("enter a size"))
l=[]
for i in range(size) :
    new_user=int(input("enter a number"))
    l.append(new_user)
print(l)

product=1
for i in range (len(l)):
    product=product*l[i]
print(product)
    
sum=0
for i in range (len(l)):
    sum=sum+l[i]
    print(sum)
    
if product<750:
    print(product)
else:
    print(sum)'''







# model 2
n=list(map(int,input("enter a number:").strip().split()))
product=1
sum=0
for i in range(len(n)):
    product=product*n[i]
    sum=sum+n[i]
if product<750 :
    print(product)
else:
    print(sum)
