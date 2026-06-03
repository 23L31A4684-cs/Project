# DAY-18

# Ordering and Ranking : Sorting Complex Data Structures

# Task-1
# You have a list of store items: products = [{"name": "Shoes", "price": 1200}, {"name": "Socks", "price": 200}, {"name": "Hat", "price": 500}]. Write a line of code using sorted() and a lambda key to sort these products by "price" from lowest to highest.
products=[
    {"name": "Shoes", "price": 1200}, 
    {"name": "Socks", "price": 200}, 
    {"name": "Hat", "price": 500}
]
prices=sorted(products,key=lambda x:x["price"])
print(prices)

# Task-2
# Given a stock log: inventory = [{"item": "Pen", "qty": 50}, {"item": "Book", "qty": 12}, {"item": "Eraser", "qty": 100}]. Sort this list by the "qty" key in descending order (highest quantity first) using reverse=True.
inventory=[
    {"item": "Pen", "qty": 50},
    {"item": "Book", "qty": 12},
    {"item": "Eraser", "qty": 100}
]
Descending_order=sorted(inventory,key=lambda y:y["qty"],reverse=True)
print(Descending_order)

# Task-3
# You have a list of users: users = [{"id": 1, "name": "Suresh"}, {"id": 2, "name": "Anil"}, {"id": 3, "name": "Charan"}]. Sort this list alphabetically by their "name" key.

users=[
    {"id": 1, "name": "Suresh"},
    {"id": 2, "name": "Anil"},
    {"id": 3, "name": "Charan"}
]
Alphabetical_order=sorted(users,key=lambda z:z["name"])
print(Alphabetical_order)
