# DAY-14

# Task

# Create a set representing your active database skills: current_db = {"Excel", "SQL", "Python"}.
#Create a second set representing a new batch of scraped skills: new_batch = {"Python", "PowerBI", "SQL", "Cloud"}.
#Create a new variable named synchronized_db and use the Union operator (|) to merge them together cleanly.
#Print synchronized_db to the terminal to verify that "Python" and "SQL" were not duplicated in the final merge

current_db={"Excel", "SQL", "Python"}
new_batch={"Python", "PowerBI", "SQL", "Cloud"}
synchronised_db=current_db | new_batch
print(synchronised_db)
