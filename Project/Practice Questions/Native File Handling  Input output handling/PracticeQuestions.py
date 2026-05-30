# DAY-9

# Task-1
# Open a file named system_boot.log in Write mode ("w") and save a line of text stating: "System initialization sequence initiated successfully."
with open("system_boot.log","w")as file:
    file.write("System initialization sequence initiated successfully.")

# Task-2
# Imagine a new job is scraped. Open the existing system_boot.log file in Append mode ("a") and add a brand-new log entry: "New Record Sync: Data Analyst Position Synced."
with open("system_boot.log","a")as file:
    file.write("New Record Sync: Data Analyst Position Synced.")

# Task-3
# You have a file called skills_inventory.txt. Write a statement to open it in Read mode ("r"), extract the entire file content into a variable named stored_data, and print it.
with open("skills_inventory.txt","r")as file:
    content=file.read()
    print(content)

# Task-4
# Open a file named salaries.txt in Read mode and use the .readlines() method to read its lines into a list called salary_rows. Print the list variable.
with open("salaries.txt","r")as file:
    contents=file.readlines()
    print(contents)

# Task-5
# Write a clean file-writing script that opens a file called vignat_test.txt in "w" mode and writes three separate lines of text, using the newline character (\n) to break them onto separate rows.
with open("vignan_test.txt","w")as file:
    file.write("Hii\n")
    file.write("Welcome\n")
    file.write("Ekeshwar...!!\n")