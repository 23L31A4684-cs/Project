# DAY-17

# Task

# Create a list of dictionaries containing inconsistent data fields:
#messy_feed = [
 #   {"item": "Laptop", "stock": 15, "warranty": "2 Years"},
  #  {"item": "Mouse", "stock": 50},  # Missing warranty
   # {"item": "Monitor", "warranty": "1 Year"}  # Missing stock
#]
#Write a for loop to step through messy_feed.
#Inside the loop, extract the "item" name using normal brackets (since every row has one).
#Extract the "stock" value using .get(), providing a default integer fallback of 0.
#Extract the "warranty" value using .get(), providing a default string fallback of "No Warranty".
#Print a structured summary string for each item showing its finalized values.

messy_feed=messy_feed = [
    {"item": "Laptop", "stock": 15, "warranty": "2 Years"},
    {"item": "Mouse", "stock": 50},  
    {"item": "Monitor", "warranty": "1 Year"}  
]

for items in messy_feed:
    stocks=items.get("stock",0)
    warrantys=items.get("warranty","No Warranty")
    print(f"stocks: {stocks} | Warranty : {warrantys}")
