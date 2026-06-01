# DAY-14

# Eliminating the Duplicated using sets

# Task-1

# You are given a list id_numbers = [101, 102, 101, 103, 104, 102]. Write the code to convert this list into a set to remove the duplicates, and print the resulting set.

id_numbers=[101, 102, 101, 103, 104, 102]
resulting_set=set(id_numbers)
print(resulting_set)

# Task-2

# Create an empty set using my_set = set(). Use the .add() method to add "Data" to it. Then use .add() to add "Data" a second time. Print the set to prove it only kept one copy.
my_set=set()
m=my_set.add('Data')
print(my_set)
#my_set=set.add("Data")
#print(my_set)

# Output : Traceback (most recent call last):
 # File "c:\Users\ekesh\Desktop\Project\Practice Questions\Eliminating Duplicates with Sets\PracticeQuestions.py", line 17, in <module>
  #  my_set=set.add("Data")
#       ^^^^^^^^^^^^^^^
# TypeError: descriptor 'add' for 'set' objects doesn't apply to a 'str' object

# Task-3

# You have two sets of applicants: java_devs = {"Alice", "Bob", "Charlie"} and python_devs = {"Bob", "Dave", "Alice"}. Write a single line of code using the Intersection operator (&) to find out exactly which applicants know BOTH languages.
java_devs={"Alice","Bob","Charlie"}
python_devs={"Bob", "Dave", "Alice"}
result=java_devs & python_devs
print(result)
