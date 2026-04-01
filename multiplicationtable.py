def main():
    number = int(input("enter number: "))
    table(number)

def table(n):
    for i in range(1,11):
        print(f"{n} X {i:2} = {n*i}")#2 for padding and table alignment
    # print(*(n*i for i in range(1,11))) # splat operator to print them seperated by spaces and also we can use wrapping in a list like list(...)

main()
