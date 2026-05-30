# DAY-11

# Error Handling Concepts

# Task-1
# Write a try/except block that attempts to divide 100 by 0. Catch the specific ZeroDivisionError and print "Math Error: Division by zero is impossible."
try:
    div=100/0
    print(f"the result of div is : { div}")
except ZeroDivisionError:
    print("Math Error: Division by zero is impossible.")

# Task-2
# Write a try/except block that tries to open a file named "ghost_data.txt" in Read ("r") mode. Catch the FileNotFoundError and print "Warning: The target dataset is missing from the directory."
try:
    with open("ghost_data.txt","r")as file:
        file.read()
except FileNotFoundError:
    print("Warning: The target dataset is missing from the directory.")

# Task-3
# You have a variable user_age = "Twenty". Try to convert it to an integer using int(user_age). Catch the ValueError and print an error message.
user_age="Twenty"
try:
    final_age=int(user_age)
    print(f"the age of the person is {final_age}")
except ValueError:
    print("Error : the string cannot be converted into integer.")

# Task-4
# You have a dictionary profile = {"role": "Analyst"}. Try to print profile["salary"]. Catch the KeyError and print "Data point not found in profile."
profile={"role":"Analyst"}
try:
    print(f"The salary of the {profile['salary']}")
except KeyError:
    print("Data point not found in profile.")

# Task-5
# Write a try/except/finally structure. In the try block, declare x = 10 / 2. In the except block, print "Failed." In the finally block, print "Execution cycle completed."
try:
    x=10/2
except:
    print("Failed.")
finally:
    print(f"Execution Cycle Completed, the Value of x is {x}")