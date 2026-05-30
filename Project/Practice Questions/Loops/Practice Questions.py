# DAY-4 #

# Loops #

# Task-1#
# The Streak Tracker: Write a for loop that loops from day 1 up to day 7 and prints out: "Day X of my learning streak completed!" (where X is the current loop number).
day=0
for day in range(0,7):
    day=day+1
    print(f"Day {day} is completed")

# Task-2 #

# A worker's starting monthly base is ₹30,000. Write a loop structure that simulates 5 consecutive annual salary reviews. Each cycle, increase their base salary tracking variable by ₹5,000 using a shortcut operator, and print out the updated salary calculation step-by-step.

intial_base=30000
for i in range(0,5):
    intial_base=intial_base+5000
    print(intial_base)

# Task-3 #

# Write a loop that counts down backward from 5 to 1, printing each number out, followed by a final print statement that says "Pipeline Triggered!".

number=5
for i in range(5,0,-1):
    print(number)
    number=number-1
print("PipeLine Triggerd!.")

# Task-4 #

# Simulate a database connection module using a while loop. Create a variable called retry_attempts and set it to 1. Keep looping as long as retry_attempts is less than or equal to 3. Inside the loop, print "Attempting connection..." and make sure to increment your counter so it doesn't loop infinitely.
retry_attempts=1
count=0
while(retry_attempts<=3):
    print("Attempt Trying....")
    retry_attempts=retry_attempts+1
    count=count+1
print(retry_attempts,count)

# Task-5

# Use a for loop combined with range() to look through numbers from 1 to 10. Inside the loop, write an if statement that checks if the number is even. Only print out the number if it is even.
for i in range(1,11):
    if i%2==0:
        print("the even number i is :",i)



