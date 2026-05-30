# DAY-6

# Task-1

# The Hub Registry: Create a dictionary named city_benchmarks containing three pairs mapping a city name to its average package: "Hyderabad" to 550000, "Bangalore" to 700000, and "Chennai" to 500000. Write a print statement displaying the average package for "Bangalore".

city_benchmarks={"Hyderabad":550000,"Bangalore":700000,"Chennai":500000}
print(city_benchmarks["Bangalore"])

# Task-2

# Tracking System Updates: Create a dictionary named pipeline_status with two keys: "total_processed": 50 and "status": "Active". Update the "status" key to read "Optimized", and add a brand new tracking key named "error_count" set to 0. Print the updated dictionary.

pipeline_status={"total_processed":50,"Status":"Active"}
pipeline_status["Status"]="Optimised"
pipeline_status["error_count"]=0
print(pipeline_status)

# Task-3

# Defensive Data Fetching: You have a dictionary: job_metrics = {"analytics_count": 113}. Use the .get() method to look up a key named "internship_count". Print the result to prove it returns None safely without crashing your script.
job_metrics={"analytics_count": 113}
print(job_metrics.get("internship_count"))

# Task-4

# Schema Inventory Extraction: Given the dictionary market_tier = {"Tier-1": "High Demand", "Tier-2": "Medium Demand", "Tier-3": "Emerging Talent"}, write two separate statements to extract and print all the keys, followed by all the values.

market_tier={"Tier-1": "High Demand", "Tier-2": "Medium Demand", "Tier-3": "Emerging Talent"}
print(market_tier.keys())
print(market_tier.values())

# Task-5

# Dictionary Initialization: Start with an empty dictionary called developer_profile = {}. Add three keys step-by-step: "name", "role", and "preferred_language", assigning your own details to them. Print the final dictionary.

developer_profile={}
developer_profile["name"]="Chinna"
developer_profile["role"]="Data Analyst"
developer_profile["preferred language"]="Telugu"
print("Updated Dictionary is: ",developer_profile)
