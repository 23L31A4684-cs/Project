# DAY-7

# Create a list filled with 4 unformatted skill names containing messy spaces and chaotic casing: dirty_skills = ["   pYtHoN   ", "  sQl  ", " eXcEl ", "   pOwErBi   "].
#Write a for loop that iterates through the dirty_skills list.
#Inside the loop, clean each item by stripping its spaces and converting it to lowercase. (Hint: You can chain methods together like .strip().lower()).
#Print each beautifully cleaned skill name out on its own line.
dirty_skills=["   pYtHoN   ", "  sQl  ", " eXcEl ", "   pOwErBi   "]
for i in dirty_skills:
   skill=i.strip().lower()
   print(skill)