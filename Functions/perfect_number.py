def perfect_number(n):
    sum=0
    for i in range(1,n+1):
        if (n%i==0):
            sum=sum+i
    return sum==n
num=int(input("enter the number: "))
print(perfect_number(num))