mylist=[]
n=int(input("enter no. of elements:"))
print("enter ",n," elements:")
for i in range(0,n):
    e=int(input())
    mylist.append(e)
print("your list:",mylist)
print("The +ve no. are :-")
for a in mylist:
    if a>0:
        print(a)
        
