# DAY-4 #

# Task-4 #

# Write a script that calculates a total sum dynamically.
#Create a variable called total_skills_hours and initialize it at 0.
#Write a loop that runs exactly 5 times.
#Each time the loop runs, pretend you studied for 2 hours and add 2 to your tracking variable using a shortcut assignment operator.
#Outside and after the loop is completely done, print out a single summary statement showing your final calculated total accumulated hours.


total_skills_hours=0
for total_skills_hours in range(5):
    total_skills_hours+=total_skills_hours+2

print("final calculated accumulated hours: ",total_skills_hours)