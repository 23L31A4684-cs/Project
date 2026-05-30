# Day-3 #
# Conditonal Statements Using (if,else) #

# Task-1 #

# A student's attendance percentage is tracked inside a variable. Write a logic routine where if the attendance falls strictly below 75, it prints out a stark text alert: "Warning: Low Attendance!". For any other percentage value, it should output: "Attendance Status: Clear".

Stu_attendance=74
if Stu_attendance>=75:
    print("Attendance Status : Clear")
else:
    print("Warning : Low Attendance !")

# Task-2 #

# An academic ranking engine classifies performance profiles. Create a decimal variable for a student's CGPA. Write a condition layout that matches and prints:
#"First Class with Distinction" if the score is 8.0 or higher.
#"First Class" if the score falls between 6.5 (inclusive) and 8.0 (exclusive).
#"Pass Class" if the score drops below 6.5.

Stu_cgpa=8.5
if Stu_cgpa>=8.0:
    print("First Class with Distinction.")
elif Stu_cgpa>=6.5 and Stu_cgpa<=8.0:
    print("First Class.")
else:
    print("Pass Class.")

# Task-3 #

# An online platform issues learning discounts based on entrance tests. If a student marks above 90, print "90% Scholarship". If they land between 70 and 90 (inclusive), print "50% Scholarship". For any lower mark configuration, print "No Discount Available".
Stu_marks=93 
if Stu_marks>=90:
    print("90% Scholarship.")
elif Stu_marks>=70 and Stu_marks<=90:
    print("50% Scholarship.")
else:
    print("No Discount Available.")

# Task-4 #

# Set up two text tracking variables: input_user and input_pass. Construct a logical comparison check using conditions ensuring that if the username equals "admin" and the password string equals "secure123", access is granted with a success text. If either parameter fails, print an error message.

input_user="admin"
input_pass="secure123"
if input_user=="admin" and input_pass=="secure123":
    print("Access Granted.")
else:
    print("Access Failed.")

# Task-5 #

# Database processing pipelines often check index positions. Create an integer variable holding a specific dataset row index number. Write a condition script using the Modulus operator (%) to compute whether the index is even or odd, and display the row's state natively.

Dataset_ind=573
# to check whether the dataset index is even or odd
if Dataset_ind%2==0:
    print("Even.")
else:
    print("Odd.")