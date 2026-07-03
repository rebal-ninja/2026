a = 8 
b = 11
target = 10 

if abs(a-target) < abs(b-target):
    print(a)
elif abs(b-target)<abs(a-target):
    print(b)
else:
    print("both are equally close ")