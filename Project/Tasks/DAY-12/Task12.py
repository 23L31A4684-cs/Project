# DAY-12

# Task
# Create an unfiltered list of raw pricing metrics: scraped_prices = [1200, -50, 3500, 0, 4200, -99].
# Write a single-line list comprehension that drops all negative entries (keeping numbers > 0) and multiplies the remaining valid values by a 1.10 calculation multiplier (representing a 10% processing markup).
# Print the finalized filtered list to the terminal screen.
scraped_prices=[1200,-50,3500,0,4200,-99]
filtered_class=[D*0.10 for D in scraped_prices if D>0]
print(filtered_class)