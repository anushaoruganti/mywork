num=int(input("ENter a number:"))
for i in range(0,num+1):
    if i%3==0 or i%8==0:
       print(i,end=" ")