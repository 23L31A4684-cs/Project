# DAY-13

# Immutable Arrays : Working with tuples

# Task-1

# Declare a tuple named server_credentials containing three items: an IP address string "192.168.1.50", a username string "admin", and a port number integer 1433.
server_credentials=("192.168.1.50","admin",1433)

# Task-2

# Try to change the port number inside your server_credentials tuple to 8080. Write down the exact error name Python throws in your terminal when you try to run it.
server_credentials[2]=8033

## Output: Traceback (most recent call last):
  #File "c:\Users\ekesh\Desktop\Project\Practice Questions\Immutable Arrays , Working with tuples\PracticeQuestions.py", line 13, in <module>
   # server_credentials[2]=8033
   # ~~~~~~~~~~~~~~~~~~^^^
# TypeError: 'tuple' object does not support item assignment

# Task-3

# Given a tuple tracking coordinate metrics: geography = (17.3850, 78.4867), write a single line of code that unpacks those values into two new variables named latitude and longitude.
geography=(17.3850,78.4867)
latitude,longitude=geography
print(latitude)
print(longitude)
