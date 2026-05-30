# DAY-5#

# Task-1

# The Job Core List: Create a list named metro_cities containing five string entries: "Hyderabad", "Bangalore", "Chennai", "Mumbai", and "Pune". Write print statements using indexes to display the very first city and the absolute last city from your list. 

metro_cities=["Hyderabad","Bangalore","Chennai","Mumbai","Pune"]
print(metro_cities[::])
print(metro_cities[::-1])

# Task-2

# Dataset Maintenance: Create a list containing four starting tech role strings: "Data Analyst", "Data Engineer", "Software Developer", and "Web Designer". Overwrite "Web Designer" with "AI Engineer" using its index position, and print the updated list.

tech_roles=["Data Analyst","Data Engineering","Software Developer","Web Designer"]
print(tech_roles[::])
print(tech_roles.index('Web Designer'))
tech_roles[3]="AI Engineer"
print("Updated List: ",tech_roles)

# Task-3

# The Growing Skillset: Start with an empty list called my_skills = []. Use the .append() method three consecutive times to add "Python", "SQL", and "Excel" into it step-by-step. Print the list and its total length using len().

my_skills=[]
my_skills.append("Python")
my_skills.append("SQL")
my_skills.append("Excel")
print(my_skills)
print(len(my_skills))

# Task-4

# Pipeline Priority Injection: You have a list of processing tasks: ['Data_Cleaning', 'Data_Visualization']. Use the .insert() method to place a new task named 'Data_Collection' at the absolute beginning (index 0) of the list. Print the result.

processing_tasks=['Data_Cleaning','Data_Visualisation']
print(processing_tasks)
processing_tasks.insert(0,'Data_Collection')
print(processing_tasks)

# Task-5

# Removing Noise Data: A list of job categories contains an irrelevant entry: ['Data Analyst', 'Business Analyst', 'Sales Executive', 'Data Scientist']. Write a statement to remove 'Sales Executive' from the list by its value name, and print the clean remaining list.

Noise_Data=['Data Analyst', 'Business Analyst', 'Sales Executive', 'Data Scientist']
print(Noise_Data)
Noise_Data.remove('Sales Executive')
print(Noise_Data)
