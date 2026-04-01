a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
result = 0
for _ in range(abs(a)):#handling negative numbers also
    result = result + b
if a < 0:
    result = -result
print(result)
#improvement
#use min(abs(a),abs(b)) in loop inside range - to handle the number iterations
#use max(ads(a),abs(b)) while adding   #as operating iterations takes more time tham addition


