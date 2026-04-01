text = input("Please enter a text: ").replace(" ","")
if text.isalnum():
    if text.isalpha():
        print("string contains only alphabets")
    elif text.isdigit():
        print("string contains only digits")
    else:
        print("string contains both alphabets and digits")
else:
    print("string may contain special characters and symbols")