#Day-2 #
#Task-2 #
#Create a variable tracking your current skills learned and set it to 0. Print it.
#On the next lines, use the shortcut assignment operator (+=) to simulate learning 2 new skills.
#Print the updated variable.
#Now, simulate that 1 skill became outdated by reducing the variable by 1 using the subtraction shortcut operator (-=).
#Print the final value to verify your code successfully altered the memory space.

Curr_skills=0
print(Curr_skills)
Curr_skills+=Curr_skills+2
print(Curr_skills)
Curr_skills-=Curr_skills-1
print(Curr_skills)