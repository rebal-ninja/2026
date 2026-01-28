n = int(input("enter n"))

reverse = 0 
while n>0:
    last_digit = n%10
    reverse = (reverse*10)+last_digit
    n//=10
print(reverse)