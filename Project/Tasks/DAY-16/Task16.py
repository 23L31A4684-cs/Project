# DAY-16

# Create a list called market_feed containing three dictionaries. Each dictionary should have "role" (text) and "years_exp" (integer).
#Make one role require 1 year, one require 4 years, and one require 2 years.
#Write a for loop that checks the "years_exp" key of every row.
#If the experience required is less than 3 years, print a string saying: "[ENTRY LEVEL FOUND]: {role}".

market_feed=[
    {"role":"Data Analyst","year_exp":1},
    {"role":"Data Engineer","year_exp":4},
    {"role":"Database Management","year_exp":2}
]
for j in market_feed:
    job_role=j['role']
    if j["year_exp"]<3:
        print(f"[ENTRY LEVEL FOUND]: {job_role}")