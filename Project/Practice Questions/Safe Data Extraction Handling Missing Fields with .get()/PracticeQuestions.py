# DAY-17

# Safe Data Extraction: Handling Missing Fields with .get()

# Task-1
# You receive a user profile dictionary: user_profile = {"username": "ekesh_9", "role": "student"}. Use the .get() method to extract the "email" key safely so that it outputs None without crashing.
user_profile={"username": "ekesh_9", "role": "student"}
email=user_profile.get("email")
print(email)

# Task-2
# Given a product metadata token: item_data = {"sku": "SKU-990", "price": 450}. Use the .get() method to look for a key named "discount". If it does not exist, make it return a default integer value of 0.
item_data={"sku": "SKU-990", "price": 450}
discount=item_data.get("discount",0)
print(discount)

# Task-3
# You have a system parameter block: system_status = {"online": True}. Try to extract a key named "maintenance_mode" using .get(). Provide a default string backup reading "Deactivated". Print the result.
system_status={"online":True}
maintenance_mode=system_status.get("maintenance_mode","Deactivated")
print(maintenance_mode)