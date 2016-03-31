import random

#k=10
#n=2**31-1
n= int(raw_input("enter fanwei num:"))
k=int(raw_input("enter K"))

x=range(0,n)
result = []
for i in range(k):
    t=random.randint(0,n)
    temp=x[i]
    x[i]=x[t]
    x[t]=temp
    result.append(x[i])
#x=random.sample(random.randint(0,2**31-1),10)
#x = random.randint(0,2**31-1)
#y=random.sample(x,10)
#list1=[random.randint(1,2**21-1)]
print result
