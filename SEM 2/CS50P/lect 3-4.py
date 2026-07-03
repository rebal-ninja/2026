import sys

if len(sys.argv) <= 1:
    print("no numbers")
    sys.exit()

total = 0
count = 0

for i in range(1, len(sys.argv)):
    try:
        num = int(sys.argv[i])
        total += num
        count += 1
    except ValueError:
        print("invalid input")
        sys.exit()

print(total / count)
