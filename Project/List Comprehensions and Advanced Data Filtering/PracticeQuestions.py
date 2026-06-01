# DAY-12

# List Comprehensions and Advanced Data Filtering

# Task-1
# Given a base list numbers = [1, 2, 3, 4, 5], write a single-line list comprehension that squares every number in the list.
numbers=[1,2,3,4,5]
square_num=[t**2 for t in numbers]
print(square_num)

# Task-2
# You have a list of calculated student marks: scores = [65, 88, 42, 95, 71]. Write a list comprehension that extracts only the scores that are greater than or equal to 75.
student_marks=[65,88,42,95,71]
extracted_scores=[z for z in student_marks if z>=75]
print(extracted_scores) 

# Task-3
# Given a list of mixed data flags: status_flags = ["Active", "Pending", "Active", "Suspended", "Active"], write a list comprehension that builds a new list containing everything except the entries that read "Suspended".
status_flags=["Active","Pending","Active","Suspended","Active"]
cleaned_flags=[s.strip() for s in status_flags if s!="Suspended" ]
print(cleaned_flags)