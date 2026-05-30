# DAY-3 #

# Task-3 Automated Profile Screener Script #

# Construct a standalone evaluation script that simulates an automatic screening mechanism for filtering entry positions.
# Create three explicit variables matching your own profile or a mock profile: knows_python (Boolean), knows_sql (Boolean), and experience_months (Integer).
# Implement an unified conditional structural rule: If the user profile holds true for either knowing Python or knowing SQL, and their cumulative experience balances out to more than 6 months, output a text stream reading "Profile Shortlisted for Tech Interview". Otherwise, return "Application archived for future cycles"

known_python=False
knows_sql=True
experience_months=3
if known_python==True or knows_sql==True:
    if experience_months>=6:
        print("Profile is Shortlisted for Tech Review.")
    else:
        print("Application archieved for future cycles.")
else:
    print("Applicant is not Eligible.")

