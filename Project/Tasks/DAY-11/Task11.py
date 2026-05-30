# DAY-11

# Task

#Define a function named robust_converter(raw_value).
#Inside the function, write a try block that attempts to convert raw_value into a float (using float()) and save it to a variable named clean_number.
#Inside the try block, immediately return clean_number.
#Write an except ValueError block underneath it. If the conversion fails, it should return "INVALID".
#Call your function twice: once passing "550.75" (print the result) and once passing "Confidential" (print the result).

def robust_converter(raw_value):
    try:
        clean_number=float(raw_value)
        return clean_number
    except ValueError:
        return "INVALID"

print(robust_converter(550.74))
print(robust_converter("Confidential"))

