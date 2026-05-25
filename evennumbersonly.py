numbers = [1,3,2,3,4,5,6,7,7,8,9,10,11,12,13,14,15]
for number in numbers:
    if number%2 != 0:
        numbers.remove(number)##wrong because it will skip some elements due to shift after removing 1 element
print(numbers)

#1
for number in numbers[:]:#right because it will iterate through entire list from first in every iteration
    if number%2 != 0:
        numbers.remove(number)
print(numbers)

#2
even_numbers=[]
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
print(even_numbers)

#3
even = [number for number in numbers if number%2==0]
print(even)