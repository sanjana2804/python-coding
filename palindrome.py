#the string after reversing should be equal 
str1=input("enter string one")
str2=input("enter string 2")
if (str1==str2[::-1]):
    print("palindrome ")
else:
    print("not a palindrome")
