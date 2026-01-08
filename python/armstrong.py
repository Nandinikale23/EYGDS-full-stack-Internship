n = int(input("Enter a number: "))
temp = n
s = 0

while n > 0:
    d = n % 10
    s = s + d*d*d
    n = n // 10

if temp == s:
    print("Armstrong number")
else:
    print("Not an Armstrong number")