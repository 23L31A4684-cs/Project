# DAY-6
 
# Analysts routinely use loops to step through dictionaries using the .items() method, which unlocks both the key and the value simultaneously.
#Create a dictionary named skill_difficulty mapping 3 skills to their complexity levels (e.g., {"Excel": "Beginner", "SQL": "Intermediate", "Python": "Advanced"}).
#Write a for loop using two tracking variables (skill, level) to iterate across skill_difficulty.items().
#Inside the loop, print out a clear sentence formatted like this: "To learn [Skill], your path context level is [Level]."

skill_difficulty={"Excel": "Beginner", "SQL": "Intermediate", "Python": "Advanced"}
for skill,level in skill_difficulty.items():
    print(f"To learn {skill}, your path context level is {level}.")