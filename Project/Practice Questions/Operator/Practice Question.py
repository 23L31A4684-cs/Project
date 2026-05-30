# Day-2 #
# Operators #

# Task-1 An analyst gets a monthly stipend of ₹25,000. Their monthly travel expense is ₹3,500 and food expense is ₹4,200. Create variables for these, calculate the remaining savings using subtraction, and print it with a clear label.
analyst=25000
expenses=3500
food=4200
remaining=analyst-expenses-food
print("Remaining Amount :",remaining)

# Task-2 You have a small dataset of 53 job postings collected from a website. You want to divide them into equal batches of 5 jobs each for analysis. Calculate and print:
#How many full batches can be created?
#How many extra job postings will be left over?

job_openings=53
equal_batches=5
no_of_batches=job_openings//equal_batches
print("Full Batches Created :",no_of_batches)
leftover_Job_postings=job_openings%equal_batches
print("Left Over Postings :",leftover_Job_postings)

# Task-3 A company sets a criteria that a student must have a graduation score of 75.0 or higher to apply. Create a variable representing a student's score (e.g., 72.5). Write a comparison expression that outputs whether the student passed the cutoff benchmark (True or False).

Grad_score=75.0
Student_score=72.5
is_true=Grad_score==Student_score
print(is_true)

# Task-4 To get a "Data Analyst Intern" interview call, a student must know Python AND have at least 1 completed project. Create two variables holding these conditions (use Booleans), combine them using the correct logical operator, and print the ultimate result.

Known_python=True
have_Completed_Project=True     #False#
Data_Analyst_Intern=Known_python and have_Completed_Project
print(Data_Analyst_Intern)      #False#

# Task-5 checked_value = 50 != 50. What value will be stored inside checked_value when this runs?
checked_value=50!=50
print(checked_value)

# The Value that is stored in the checked_value is False because the condition 50!=50 is failed so hence the checked_value stores False Value in it. #