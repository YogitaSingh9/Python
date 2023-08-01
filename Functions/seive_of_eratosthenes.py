def soe(num):
    prime_list=[]
    for i in range(2,num+1):
        if i not in prime_list:
            print(i)
            for j in range(i*i,num+1,i):
                prime_list.append(j)
print(soe(50))