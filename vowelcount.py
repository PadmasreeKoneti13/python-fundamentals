vowels = "aeiou"
string = input("Enter a string: ").lower()
count=0
for char in string:
    if char in vowels:
        count += 1
print(count)

#trying even or odd in pythonic way

num = int(input("enter number:"))
# if num % 2 == 0:
#     print(f"{num} is an even number")
# else:
#     print(f"{num} is not an even number")
print("even" if num % 2 == 0 else "odd")


#improvement pythonic of vowel problem
# count = sum(1 for char in string if char in vowels)
# total_vowels = sum(string.count(v) for v in vowels)
#if we use sets to store vowels then the speed will be better as in real world applications more strings(longer) are there