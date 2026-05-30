# DAY-9

# Task

#Create a list of three premium core skills: priority_skills = ["Machine Learning", "Cyber Law", "Data Engineering"].
#Use a context manager to open a new file named production_targets.txt in Write mode.
#Inside the file context, write a for loop that steps through your priority_skills array.
#On each turn of the loop, write the skill into the file on its own line (Hint: Use an f-string or add + "\n" to push each word to a new row).

priority_skills=["Machine Learning","Cyber Law","Data Engineering"]
with open("production_targets.txt","w")as file:
    for i in priority_skills:
        file.write(f'the new skill is {i} \n')
