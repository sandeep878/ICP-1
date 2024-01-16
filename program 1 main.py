def process_string(input_string):
    characters = list(input_string)
    if len(characters) >= 4:
        characters = characters[::2]
        characters.reverse()
        reversed_string = ''.join(characters)
        print("Reversed String:", reversed_string)
    else:
        print("Input string should have at least 4 characters.")

def performing_4_arithmetic_operations(num1, num2):
    print(f"Addition = {num1+num2}")
    print(f"Subtraction = {num1 - num2}")
    print(f"Multiplication = {num1 * num2}")
    if num2 != 0:
        print(f"Division = {num1 / num2}")
    else:
        print("Cannot divide by zero.")
input_string = input("Enter a string: ")
process_string(input_string)
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
performing_4_arithmetic_operations(num1, num2)
