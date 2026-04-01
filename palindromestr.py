string = input("Enter a string: ")
# if string == string[::-1]:
#     print("The string is palindrome")
# else:
#     print("The string is not palindrome")
n = len(string)
is_palindrome = True
for i in range(n//2):
    if string[i] != string[n-i-1]:
        is_palindrome = False
        break
if is_palindrome:
    print(f"{string} is a palindrome")
else:
    print(f"{string} is not a palindrome")

