# DAY-8

# Task-1
#You have a file configuration string: filename = "backup_dataset.csv". Write a statement checking if the file ends with ".csv". Print the True/False result.
filename="backup_dataset.csv"
print(filename.endswith(".csv"))

# Task-2
# A web scraper extracted a raw price string: scraped_value = "450000". Write a statement using a validation method to confirm if the value is made entirely of digits.
scraped_value="450000"
print(scraped_value.isdigit())

# Task-3
# Another scraped variable returned scraped_bonus = "50K". Run the .isdigit() check on this string and print the result to demonstrate why it fails.
scraped_bonus="50k"
print(scraped_bonus.isdigit())  # Output is False

# The result is false beacuse the string contains combination of both digit and characters hence the result is false

# Task-4
# A corporate recruitment log string states: log_id = "JOB_POST_2026". Write a line checking if this tracking ID starts with the exact token prefix "JOB".
log_id="JOB_POST_2026"
print(log_id.startswith("JOB")) # output is True

# Task-5
# Given two variables, course = "Machine Learning" and completion_percentage = 85, use an f-string to print a message matching this exact text: "Your study module for Machine Learning is 85% complete."
course="Machine Learning"
completion_percentage=85
print(f"Your study module for {course} is {completion_percentage}% completed.")
