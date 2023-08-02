def armstrong(num):
    sum=0
    t=num
    while(t>0):
        digit=t%10
        sum+=digit**3
        t//=10
    if(num==sum):
        print("YES, it is an armstron number!")
    else:
        print("NO, it is not an armstrong number!")
n=int(input("enter the number you want to check: "))
print(armstrong(n))
