x=int(input("enter a number :-"))
reverse =0
temp = x
while x>0:
    remainder = x % 10
    reverse = reverse * 10 + remainder
    x = x//10
if reverse == temp :
    print("number is palindrome ")
else:
    print("number is not palindrome ")       
