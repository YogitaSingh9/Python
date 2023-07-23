'''You are given a string and your task is to swap cases. 
In other words, convert all lowercase letters to uppercase letters and vice versa.'''
def swap_case(s):
    r=''
    for i in s:
        if i.isupper():
            r=r+i.lower()
        else:
            r=r+i.upper()
    return r

        
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)