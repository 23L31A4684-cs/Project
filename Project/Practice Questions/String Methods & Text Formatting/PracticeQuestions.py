# DAY-7

# Task-1
# A student registered with accidental spaces: user_email = "  ekeshwar@vignaniit.edu.in  ". Write a statement using a string method to strip away the trailing spaces and print the clean output.

user_email="  ekeshwar@vignaniit.edu.in  "
print(user_email.strip())

# Task-2

#A job board returned a mixed-case title: scraped_title = "mAcHiNe LeArNiNg EnGiNeEr". Convert this string entirely into uppercase characters using a string method and print the result.

scraped_title="mAchiNe LeArNiNg EnGiNeEr"
print(scraped_title.upper())

# Task-3

#A data row contains an outdated tool name: pipeline_record = "Data visualization tracking completed via Tableau". Use the .replace() method to switch the word "Tableau" to "PowerBI", and print the updated record string.

pipeline_record="Data visualization tracking completed via Tableau"
updated_pipeline_record=pipeline_record.replace("Tableau","Power BI")
print(updated_pipeline_record)

# Task-4

#You have a long text description string: job_summary = "Must be proficient in advanced SQL database querying and query optimization.". Write a conditional statement checking if the keyword "SQL" is present in the text, and if it is, print "Keyword Match Found!".

job_summary="Must be proficient in advanced SQL database querying and query optimization."
c=("SQL" in job_summary)
if c==True:
    print("Keyword match is found!!")
else:
    print("Not found!!")

# Task-5

#Take the raw lowercase entry city_entry = "hyderabad" and convert it into a professional proper-noun title format (where the 'H' is capitalized) using a single string method.
city_entry="hyderabad"
print(city_entry.title())

