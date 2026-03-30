a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
if a>=b and a>=c:
    print(f"The largest number is {a}")
elif b>=c:
    print(f"The largest number is {b}")
else:
    print(f"The largest number is {c}")
