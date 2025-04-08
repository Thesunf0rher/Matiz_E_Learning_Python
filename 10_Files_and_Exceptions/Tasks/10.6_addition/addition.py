def addiction(num1, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
    except ValueError:
        print("Enter a number, not a text.")
    else:
        print(num1 + num2)

addiction(6,100)
addiction(6,'asd')