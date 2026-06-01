# DAY-15

# Multi Dimensional Iterations --> Nested Loops

# Task-1

# Write an outer loop that runs from 1 to 3 (representing the X-axis) and an inner loop that runs from 1 to 3 (representing the Y-axis). Print out the coordinates
for x in range(1,4):
    for y in range(1,4):
        print(f"{x,y}")

# Task-2
# You have a 2D matrix of salaries: salary_tiers = [[400, 500], [700, 800], [1000, 1200]]. Write a nested loop that prints every single salary number individually.
salary_tiers = [[400, 500], [700, 800], [1000, 1200]]
for x in salary_tiers:
        for y in x:
            print(y)

# Task-3
# You have a list of two phrases: phrases = ["Data", "SQL"]. Write an outer loop to step through the phrases, and an inner loop to step through every single letter in those phrases. Print each letter one by one.

phrases=["Data","SQL"]
for z in phrases:
     for w in z:
          print(w)