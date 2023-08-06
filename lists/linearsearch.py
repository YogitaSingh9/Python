def linear(n,x,size):
    for i in range(0, size):
        if (n[i]==x):
            return i
        return -1
ar = [ 1,2,3,4,5,6,7,88]
print(ar)
length=len(ar)
y=int(input("enter the element to be searched: "))
answer = linear(ar,y,length)
if( answer == -1):
    print("element not found ")
else:
    print("elemet found at ",answer)
    