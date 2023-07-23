'''commission on sales by salesman is calculated as [er the following policy
amount of sale (in ₹)       Commission Rate
0-5000                           nil
5001-10000                  5% excess of 5000
10001-15000                7.5% excess of 10000 
>15000                     10% excess of 15000
print the sales made by salesman and display the commission due.'''
sales=int(input("enter the sales in ₹ "))
if(sales<=5000):
    commission=0
elif(sales<=10000):
    commission=(sales-5000)*0.05
elif(sales<=15000):
    commission=250+(sales-10000)*0.075
else:
    commission=1000+(sales-15000)*0.1
print('Coumpound commission in ₹',commission)
