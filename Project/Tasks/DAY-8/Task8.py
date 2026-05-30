# DAY-8

# Create a list containing five mixed data input entries: raw_inputs = ["500000", "650000", "Undisclosed", "720000", "Negotiable"].
#Write a for loop that steps through the raw_inputs list.
#Inside the loop, write an if-else statement:
#If the entry is completely numeric (.isdigit()), print: "Valid Salary Column Data: [Entry]"
#If it contains text letters or non-digits, print: "Alert: Invalid Text Data Found: [Entry]" 

raw_inputs=["500000", "650000", "Undisclosed", "720000", "Negotiable"]
for i in raw_inputs:
    if (i.isdigit())==True:
        print(f"Valid Salary Column Data: {i}")
    else:
        print(f"Alert:Invalid Text Data Found {i}")