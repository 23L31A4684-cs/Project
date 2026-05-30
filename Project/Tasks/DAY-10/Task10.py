# DAY-10

# Task

# Define a function named clean_skill_entry(raw_skill).
# Inside the function, create a variable called formatted_skill that strips the spaces and converts raw_skill to title case (.title()).
# return the formatted_skill variable.
# Outside the function, create a test variable: messy_input = "   mAcHiNe lEaRnInG   ".
# Call your function, pass messy_input into it, save the result to a new variable, and print it to prove it cleaned it perfectly

def clean_Skill_entry(raw_skill):
    formatted_skill=raw_skill.strip().title()
    return formatted_skill
message_input="   mAcHiNe lEaRnInG   "
result=clean_Skill_entry(message_input)
print("The input message is properly cleaned :",result)