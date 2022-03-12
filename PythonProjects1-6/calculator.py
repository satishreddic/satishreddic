# Python program for simple calculator
  
# Function to add two numbers 
def add(input1, input2):
    return input1 + input2
  
# Function to subtract two numbers 
def subtract(input1, input2):
    return input1 - input2
  
# Function to multiply two numbers
def multiply(input1, input2):
    return input1 * input2
  
# Function to divide two numbers
def divide(input1, input2):
    return input1 / input2
  
print("Please select an option from the following-\n" \
        "1. Addition\n" \
        "2. Subtraction\n" \
        "3. Multiplication\n" \
        "4. Division\n")
  
# Take input from the user 
option = int(input("Select operations form 1, 2, 3, 4 :"))

input_1 = int(input("Please provide first input : "))
input_2 = int(input("Please provide second input: "))
  
if option == 1:
    print("The addition of two numbers is:",input_1, "+", input_2, "=",
                    add(input_1, input_2))
  
elif option == 2:
    print("The subtraction of two numbers is:",input_1, "-", input_2, "=",
                    subtract(input_1, input_2))
  
elif option == 3:
    print("The multiplication of two numbers is:",input_1, "*", input_2, "=",
                    multiply(input_1, input_2))
  
elif option == 4:
    print("The division of two numbers is:",input_1, "/", input_2, "=",
                    divide(input_1, input_2))
else:
    print("You have selected an invalid option")