n = int(input("enter n"))

rev = 0 
dup = n

while n>0:
    last_digit = n%10
    rev = (rev*10)+last_digit 
    n//=10

print(rev)

if dup==rev:
    print("the given number is a palindrom")
else:
    print("it is not a palindrom")