sample = ['Hey' ,'everyone', 'this', 'is', 'python' ,'programs' ,'repo']
print("The original list is : " + str(sample))
res = [sub.replace('O', '-').replace('e', 'G').replace('-', 'e') for sub in sample]

print ("List after performing character swaps : " + str(res))
