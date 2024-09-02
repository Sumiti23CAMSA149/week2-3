n=int(input("enter a integer :-"))
sum=0
while n>0:
    rev = n%10
    sum +=rev
    n =n//10
print(sum)    