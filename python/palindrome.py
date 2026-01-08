#palindrome using slicing 
'''num = input("Enter a number: ")

if num == num[::-1]:
    print("Palindrome number")
else:
    print("Not a palindrome number")'''
    
        # OR
    
num = input("Enter a no: ")
rev = ""

for ch in num:
    rev = ch + rev

if num == rev:
    print("Palindrome")
else:
    print("Not Palindrome")