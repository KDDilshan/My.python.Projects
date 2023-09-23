import random

print(" '''''''Remember input only positive integer values 1-100'''''''")
x=int(input("Enter the first no of range      : "))
y=int(input("Enter the second no of the range : "))
z=int(input("Enter the no of chances you need :"))
print("'''''''''''''''''''''''''''''''''''''''''''")


n=random.randint(x,y)
count=0
while count<z:
    no=int(input("guess a number from your selected range: "))
    if(no==n):
        print("congraulations!!!  you are correct")
        break
    elif(no>n):
        print("too high")
    elif(no<n):
        print("too low")
    count=count+1
    print(f"your {count}st chance")
else:
    print("better try next time '(-_-)'")
    quit()
print(f"you have done it in {count} chanceses")