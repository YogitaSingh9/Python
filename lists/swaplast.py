sample = ['Hey' ,'everyone', 'this', 'is', 'python' ,'programs' ,'repo']
print("The original list is : " + str(sample))
res = [sub.replace('O', '-').replace('i', 'n').replace('-', 'p') for sub in sample]

print ("List after performing character swaps : " + str(res))
