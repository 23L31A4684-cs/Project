# DAY-10

# Functions

# Task-1
# Define a simple function called boot_yuksatra_node() that takes no parameters. Inside it, print the text "Team Yuksatra: Node Initialized". Then, write the line of code to call this function.
def boot_yuksatra_node():
    print("Team Yuksatra : Node Initialized.")

boot_yuksatra_node();

# Task-2
# Create a function called log_student(registration_number) that accepts one parameter. Inside the function, use an f-string to print: "Student ID {registration_number} logged into the system." Call the function using the ID "23LA1A0511".
def log_student(registration_number):
    print(f"Student ID {registration_number} logged into the system.")

log_student("23L31A4684")

# Task-3
# Write a function named calculate_bonus(base_pay) that multiplies the base_pay by 0.10 and returns the result. Call the function with 600000 and save the result into a variable named my_bonus. Print my_bonus
def bonus_calculation(payment):
    bonus=payment*0.10;
    return bonus
final_amount= bonus_calculation(345870)
print("Bonus Amount :",final_amount)

# Task-4
# Create a function called format_course(unit, topic) that takes two parameters. Make it return an f-string like: "Unit [unit] covers [topic].". Call it passing 5 and "Clustering". Print the result.

def format_course(unit,topic):
    print(f"Unit {unit} covers Topic {topic} ")

format_course(5,"Clustering")

# Task-5
# If you write def set_database(db_name="Local_SQL"):, the function will use "Local_SQL" if you forget to pass a parameter. Write a function called connect_server(server_ip="192.168.1.1") that prints "Connecting to {server_ip}". Call it once normally with "10.0.0.5", and call it a second time with empty parentheses to see the default kick in.
def set_database(db_name="Local_SQL"):
    print(f"The system uses database {db_name}")
def connect_server(server_ip="192.168.1.1"):
    print(f"Connecting to {server_ip}")

set_database()
connect_server("10.0.0.1")
connect_server()
    