class Calculator:
    def addiction(self):
        while True:
            try:
                num1 = input("Enter a num: ")
                if num1 == 'q':
                    break
                num1 = int(num1)

                num2 = input("Enter a num: ")
                if num2 == 'q':
                    break
                num2 = int(num2)

            except ValueError:
                print("Enter a number, not a text.")
            else:
                print(f"Result: {num1 + num2}")

calc = Calculator()
calc.addiction()