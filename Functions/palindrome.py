def palindrome(string):
  rev = ''.join(reversed(string))
  if (string == rev):
    print(string,'is a Palindrome')
  else:
    print(string,'is not a Palindrome')
str=input("Enter the string : ")
palindrome(str)
