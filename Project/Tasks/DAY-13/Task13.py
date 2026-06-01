# DAY-13

# Task

# Create a fixed tuple tracking your analysis constants: MARKET_CONSTANTS = (0.5, "INR", "Vignan-IIT"). These represent your job processing minutes, local currency profile, and target educational institute.
#Unpack the MARKET_CONSTANTS tuple into three variables named runtime_factor, currency_code, and campus_id.
#Use an f-string to print a clean confirmation statement to your terminal console layout: f"[CONFIG LOADED]: Processing for {campus_id} using currency {currency_code}."

MARKET_CONSTANTS=(0.5,"INR","Vignan-IIT")
runtime_factor,currency_code,campus_id=MARKET_CONSTANTS
print(f"[CONFIG LOADED]: Processing for {campus_id} using currency {currency_code}.")