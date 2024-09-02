x = int(input("enter a starting number :-"))
y = int(input("enter a ending number :-"))

for i in range(x,y+1):
    if i>1:
        for j in range(2,i//2):
          if i%j == 0:
            break
        else: 
            print(i)
