# Student Job Market Analyzer with AI Insights #
#Project Begins Day-1 #

# Project Title #
Project_Title="Student Job Market Analyzer with AI Insights"
# Developer Details #
Developer_name="NAKKINA EKESHWAR"
# Project Deployment Days #
Total_Days=270
curr_Day=1
is_Dashboard_created=False

# Display Remaining Days #
req_days=Total_Days-curr_Day
print(req_days)

#Display all the Variables

print("System is Booting Up......")
print("Project Title :",Project_Title)
print("Developer Name :",Developer_name)
print("Total Days :",Total_Days)
print("Current Day :",curr_Day)
print("DashBoard Created :",is_Dashboard_created)
print("Required Days for Deployment :",req_days)

# Day-2 #
# Task of DAY-2 / DAY-270 #
#Keep Your Day 1 Progress: Retain all your system variables (Title, Developer Name, Day tracker, etc.) at the top.
#Add Raw Data Metrics: Create new integer variables representing raw job data counts:
#total_scraped_jobs: set it to a starting estimation of 145.
#unfiltered_internships: set it to 32 (these are entries that aren't full-time positions).
#Calculate Clean Data: Create a new variable called clean_analyst_jobs. Use an arithmetic operator to calculate this value by subtracting the internships from the total scraped jobs.
#Calculate Processing Time: Assume that your system takes exactly 0.5 minutes (Float) to clean and process a single job entry. Create a variable called total_processing_minutes and calculate the time needed to process all your clean_analyst_jobs using multiplication.
#Display the Metrics: Add a clean visual separator line using symbols (like print("-" * 30) or just typing characters inside a string) and print these new operational statistics underneath your Day 1 system summary text.

total_Jobs=145
unfiltered_internships=32
cleaned_analyst_Jobs=total_Jobs-unfiltered_internships
Processing_Time=cleaned_analyst_Jobs*0.5
print("DAY-2 : ")
print("Total_Jobs :",total_Jobs)
print("internhsips :",unfiltered_internships)
print(cleaned_analyst_Jobs)
print(Processing_Time)

# DAY-3 #
# Task of DAY-3/DAY-270#
#Now that your local processing program can safely extract counts and calculate time dimensions, it needs to evaluate the magnitude of the workload autonomously and output condition logs onto your monitoring console.
#Bring Forward Your Consolidated Baseline: Pull down your project identification variables from Day 1, along with your verified math metrics from Day 2 (ensuring cleaned_analyst_Jobs = total_Jobs - unfiltered_internships is cleanly applied).
#Establish Data Density Threshold Conditions: Directly beneath your terminal variable outputs, build an integrated conditional branching scheme (if-elif-else) that directly evaluates the internal volume stored inside your cleaned_analyst_Jobs calculation.
#Define System Output Statements
#If cleaned_analyst_Jobs is strictly greater than 100, execute a print instruction showing this custom operational code: "[SYSTEM STATUS]: High dataset volume detected. Core optimization script initialized."
#If cleaned_analyst_Jobs is positioned between 50 and 100 inclusive, execute a print statement showing: "[SYSTEM STATUS]: Normal dataset volume detected. Standard processing pipeline active."
#If the volume value runs lower than 50, pass execution to a block that prints: "[SYSTEM STATUS]: Low dataset volume detected. Fast-track execution context loaded."
#Execute and Validate: Run your total script file. Since your current tracking variable resolves dynamically to 113, make sure your conditional system successfully captures that threshold branch and triggers the High dataset volume statement

if cleaned_analyst_Jobs>100:
    print("[SYSTEM STATUS]: High dataset volume detected. Core optimization script initialized.")
elif cleaned_analyst_Jobs>=50 and cleaned_analyst_Jobs<=100:
    print("[SYSTEM STATUS]: Normal dataset volume detected. Standard processing pipeline active.")
else:
    print("[SYSTEM STATUS]: Low dataset volume detected. Fast-track execution context loaded.")

# DAY-4 #

# Task of DAY-4/DAY-270#

#Preserve Your Script Core: Pull down your project title variables from Day 1, your math expressions from Day 2, and your corrected baseline condition alerts from Day 3.
#Define Batch Properties: Create a new integer variable called total_data_batches and set its value to 5.
#Simulate Batch Ingestion Iteration: Create a clear visual separator in your print log console. Directly beneath it, write a loop that will run exactly as many times as your total_data_batches variable dictates.
#Print Sequential Progress Logs: Inside your loop block, print an explicit status message detailing which exact dataset batch is currently being processed by the pipeline. For example, it should print:
#Processing Dataset Batch 1/5...
#Processing Dataset Batch 2/5...
#... all the way until it completes batch 5.
#Finalize Process Summary: Outside of the loop (make sure it is not indented), write a final terminal log line printing a closing notification, such as "[SUCCESS]: All 5 job data batches successfully synchronized into the system architecture."

total_data_batches=5
for total_data_batches in range(1,6):
    print(f"Processing Dataset Batch {total_data_batches}/5 ")
print("[SUCCESS]: All 5 job data batches successfully synchronized into the system architecture.")

# DAY-5

# Task of DAY-5/DAY-270

#Initialize the Skills Tracker List: Create a new list variable named extracted_skills_pool containing three initial base core items: "Excel", "SQL", and "PowerBI".
# Simulate Real-time Job Scraping Additions: Imagine your engine scanned a new job posting from Hyderabad that requires programming expertise. Use the .append() method to add "Python" to your list.
# Inject AI Core Requirements: Use the .insert() method to place "Generative AI" at index 1 of your list to mark it as an immediate high-priority track asset.
# Print Database Inventories: Create a neat separator line ("-" * 40) and print out your updated skill pool dataset along with a message stating: f"Total Core Market Skills Tracked: {len(extracted_skills_pool)}"

extracted_skills_pool=["Excel","SQL","PowerBI"]
extracted_skills_pool.append('Python')
extracted_skills_pool.insert(1,"Generative AI")
print("-"*40)
print(extracted_skills_pool)
print(f"Total Core Market Skills Tracked: {len(extracted_skills_pool)}")


# DAY-6

# Task of DAY-6/DAY-270

#Consolidate Project Identity metadata: Create a new dictionary variable named system_meta_profile. Populate it with these initial structural key-value attributes:
#"title": "Student Job Market Analyzer with AI Insights"
#"developer": "EKESHWAR NAKKINA"
#"target_database": "SQL_Local_Instance"
#Inject Runtime Statistics Dynamically: Add a new key to your system_meta_profile dictionary named "verified_jobs_volume" and assign your calculated cleaned_analyst_Jobs metric variable directly to it.
#Perform a Safe Feature Flag Lookup: Use the .get() method to look up a key named "is_cloud_deployed" inside your dictionary. Assign this returned result to a temporary variable and print it out to verify your configuration structure checks out safely.
#Print Complete System Blueprint Configurations: Print a clean header, and output your updated system_meta_profile dictionary to the terminal to display your unified system metrics inventory tracking panel.

system_meta_dataprofile={"title":"Student Job Market Analyzer with AI Insights.","developer":"EKESHWAR NAKKINA","target_database":"SQL_Local_Instance"}
system_meta_dataprofile["verified_job_profiles"]="20%"
result=system_meta_dataprofile.get("is_cloud_deployed")
print(result)
print("Updated profiles:",system_meta_dataprofile)


# DAY-7

# Task of Day-7 / Day-270

#Initialize Raw Scraping Payload: Create a new string variable named raw_payload_title and assign it this exact messy string:
#"   SYSTEM REQUIREMENT: senior data analyst Specialist (MySQL)   "
#Sanitize Layout Spaces & Boundaries: Apply the .strip() method to remove the massive padding blocks from the ends of raw_payload_title.
#Enforce System Standardization Rules: Use the .replace() method to swap out the outdated database tag "(MySQL)" with our current active database profile target "(SQL_Local_Instance)".
#Normalize Text Tier Case: Convert the entire sanitized string into clean, readable Title Case styling.
#Print Clean Production Logs: Print out a separator line and log the finalized text string to the console labeled cleanly like this: f"Sanitized Ingestion Title Profile: {final_clean_title}".

raw_payload_title="   SYSTEM REQUIREMENT: senior data analyst Specialist (MySQL)   "
print("Updated Title:",raw_payload_title.strip())
print("Replaced Title:",raw_payload_title.replace("MySQL","SQL_Local_Instance"))
final_clean_title=(raw_payload_title.title())
print(f"Sanitized Ingestion Title Profile: {final_clean_title}")


# DAY-8

# Task of Day-8/Day-270

#Create two new string variables mimicking raw data pulled from a web page:
#scraped_salary_1 = "550000"
#scraped_salary_2 = "650,000" (Notice the sneaky comma character!)
#Construct Ingestion Validation Logic Gates: * Write an if-else condition testing if scraped_salary_1 is completely numeric. If it is, use an f-string to log: f"[DATABASE INGESTION]: {scraped_salary_1} passes validation checks. Writing to target database...".
#Write a second if-else condition testing if scraped_salary_2 is numeric. If it isn't, use an f-string to log: f"[DATA CORRUPTION ALERT]: Entry '{scraped_salary_2}' contains invalid characters. Routing to error audit logs...".
#Assemble and Print Unified Outputs: Run your master file to ensure all your automation metrics, loop states, skill lists, metadata profiles, and new safety validation gates execute cleanly on one unified terminal screen.

scraped_salary_1="550000"
scraped_salary_2="650,000"
if (scraped_salary_1.isnumeric()):
    print(f"[DATABASE INGESTION]: {scraped_salary_1} passes validation checks. Writing to target database...")
else:
    print("Invalid Entry Found.")

if (scraped_salary_2.isnumeric()):
    print(f"[DATABASE INGESTION]: {scraped_salary_2} passes validation checks. Writing to target database...")
else:
    print(f"[DATA CORRUPTION ALERT]: Entry '{scraped_salary_2}' contains invalid characters. Routing to error audit logs...")
    
# DAY-9

# Task of Day-9/Day-270

#Construct an Audit String Payload: Create a single, clean f-string summary variable named audit_log_entry that captures today's current state. It should combine your metadata text block and your data results into one long text summary:
#audit_log_entry = f"PROJECT: {project_title} | DEVELOPER: {developer_name} | STATUS: Active | VALID RECORDS CALCULATED: {cleaned_analyst_Jobs}\n"
#Commit the State to Disk: Use the context manager with open("pipeline_audit.txt", "a") as audit_file: to open or create a file named pipeline_audit.txt. Append your audit_log_entry string directly into it.
#Verify via Read Actions: Write a second, separate file execution block that opens pipeline_audit.txt in Read mode ("r"), reads out its contents, and prints a console notification confirming execution: print("[AUDIT FILE VERIFIED]:\n", audit_file.read()).

audit_log_entry=f"Project : {Project_Title} | Developer : {Developer_name} | Status : Active | Valid Records Calculated : {cleaned_analyst_Jobs}\n"
with open("pipeline_audit.txt","a") as audit_file:
    audit_file.write(audit_log_entry)
with open("pipeline_audit.txt","r") as audit_file:
    audit_file.read()
    print("[AUDIT FILE VERIFIED]:")


# DAY-10

# Task of Day-10/Day-270

# Define the Validation Function: At the very top of your script (right under your initial variables), create a new function: def validate_salary(salary_string):
#Inject the Logic: Move your if/else .isdigit() checking logic from Day 8 inside this new function.
#If it is a digit, have the function return True.
#If it is NOT a digit, have the function return False.
#Deploy the Function: Down in your main execution area, use your new function to test your variables

def salary_validation(salary_string):
    if salary_string.isdigit():
        return True
    else:
        return False
result1=salary_validation("50k")
result2=salary_validation("100000000")

print(result1)
print(result2)

# DAY-11

# Task of Day-11/Day-270

#Wrap the File Reader: Locate your file-reading execution block from Day 9 (the one that opens pipeline_audit.txt in "r" mode to verify it).
#Apply the Safety Net: Wrap that entire with open(...) file-reading block inside a try statement.
#Catch the Crash: Add an except FileNotFoundError: block. If the file goes missing, instead of the system crashing, print a clean professional warning: "[SYSTEM OVERRIDE]: Audit file not found. Booting with a fresh slate."
#Test the Armor: To test if your armor works, temporarily change the file name in your try block to "fake_audit_file.txt" and run your master script. It should trigger your custom warning instead of a massive red Python crash terminal

try:
    with open("pipeline_audit.txt","r")as files:
        files.read()
        print("pipeline_audit.txt read successfully.")
except FileNotFoundError:
    print("[SYSTEM OVERRIDE]: Audit file not found. Booting with a fresh slate.")

# DAY-12

# Task of Day-12/Day-270

#senting skills captured from a live data feed:
#incoming_raw_pool = ["  Excel ", "Python", "  SQL ", "PowerBI", "Generative AI", "Tableau", "  Machine Learning "]
#Refactor with Comprehensions: Write a single, optimized list comprehension line named optimized_skills_dataset.
#It must run .strip() on every skill to clean the messy spaces.
#It must use an if condition at the end to filter out "Excel" and "Tableau" (since we want to isolate only advanced coding/analytical assets).
#Display the Output: Print a clean visual header line and display your freshly compressed optimized_skills_dataset list to verify it works perfectly.

incoming_raw_pool=["  Excel ", "Python", "  SQL ", "PowerBI", "Generative AI", "Tableau", "  Machine Learning "]
operation=[optimised_skill_dataset.strip() for optimised_skill_dataset in incoming_raw_pool if optimised_skill_dataset.strip() not in ["Excel","Tableau"]]
print(operation)


# DAY-13

# Task of Day-13/Day-270

# Create a permanent tuple named PIPELINE_INFRASTRUCTURE containing three fixed items mapping our exact engine properties:
#PIPELINE_INFRASTRUCTURE = ("SQL_Local_Instance", "pipeline_audit.txt", 1.10)
#(These represent your target SQL database, your audit file name from Day 9, and your price markup multiplier from your Day 12 hands-on tasks).
#Unpack the Infrastructure Constants: On the very next line, write an unpacking statement to map those three hidden tuple values into three clearly named variables: target_db, log_filename, and markup_factor.
#Display System Ingestion Parameters: Print a clean header console log section labeled "--- DAY 13: CORE INFRASTRUCTURE LOCKS ---" and print out your newly unpacked target_db and log_filename variables to confirm they are active and fully protected.

PIPELINE_INFRASTRUCTURE=("SQL_Local_Instance", "pipeline_audit.txt", 1.10)
target_db, log_filename,markup_factor=PIPELINE_INFRASTRUCTURE
print("--- DAY 13: CORE INFRASTRUCTURE LOCKS ---")
print(target_db)
print(log_filename)
print(markup_factor)


# DAY-14

# Task of Day-14/Day-270

# Create a new list containing a mix of new skills and skills we already have:
#Convert Arrays to Sets: We need to convert both our Day 12 array and our new array into sets so we can merge them:
#Create set_1 = set(optimized_skills_dataset) (This pulls your clean array from Day 12)
#Create set_2 = set(batch_2_raw_skills)
#Execute the Union Merge: Create a new variable named master_unique_skills and use the Union operator (|) to combine set_1 and set_2.
#Display System Output: Print a clean header log --- DAY 14: DEDUPLICATION ENGINE --- and print out your final master_unique_skills set to prove to the system that all overlaps (like Python and SQL) were safely eliminated.

batch_2_raw_skills = ["SQL", "Cloud Computing", "Python", "Data Warehousing", "PowerBI"]
Create_set1=set(PIPELINE_INFRASTRUCTURE)
Create_set2=set(batch_2_raw_skills)
master_unique_skills=Create_set1 | Create_set2
print("--- DAY 14: DEDUPLICATION ENGINE ---")
print(master_unique_skills)


# DAY-15

# Task of DAY-15/DAY-270

# Create a 2D array representing three different web-scraping batches containing job skills:
#multi_batch_stream = [
 #   ["SQL", "Python", "Data Modeling"],
  #  ["PowerBI", "SQL", "Excel"],
   # ["Machine Learning", "Python", "Cloud"]
#]
##Initialize a Master Storage Set: Create an empty set named global_unique_skills = set(). We will use this to automatically destroy duplicates as our nested loop runs.
#Build the Nested Extraction Loop: * Write an outer for loop to step through the batches in multi_batch_stream.
#Write an inner for loop to step through every skill inside the current batch.
#Inside the inner loop, add the skill to your global_unique_skills set using the .add() method.
#Display System Output: Print a clean header log --- DAY 15: MULTI-LAYERED INGESTION ENGINE --- and print your finalized global_unique_skills set.

multi_batch_stream = [
    ["SQL", "Python", "Data Modeling"],
    ["PowerBI", "SQL", "Excel"],
    ["Machine Learning", "Python", "Cloud"]
]

globla_unique_cells=set()
for batches in multi_batch_stream:
    for skill in batches:
        c=globla_unique_cells.add(skill)
    
print("--- DAY 15: MULTI-LAYERED INGESTION ENGINE ---")
print(globla_unique_cells)

scraped_job_postings=[
    {"job_id": 5001, "role": "Data Analyst", "core_skill": "SQL"},
    {"job_id": 5002, "role": "Backend Dev", "core_skill": "Java"},
    {"job_id": 5003, "role": "BI Developer", "core_skill": "PowerBI"}
]
for job in scraped_job_postings:
    job_id = job["job_id"]
    role = job["role"]
    core_skill = job["core_skill"]
    if core_skill in globla_unique_cells:
        print(f"[SKILL MATCH] Candidate profile aligns with {role} (ID: {job_id})")

# DAY-16

# Task of Day-16/Day-270

# Simulate a Structured Data Feed: Create a new list called scraped_job_postings that contains three dictionaries. Each dictionary must have three keys: "job_id", "role", and "core_skill".
#Example Row 1: {"job_id": 5001, "role": "Data Analyst", "core_skill": "SQL"}
#Example Row 2: {"job_id": 5002, "role": "Backend Dev", "core_skill": "Java"}
#Example Row 3: {"job_id": 5003, "role": "BI Developer", "core_skill": "PowerBI"}
#Build the Analytics Matcher: Write a for loop to step through scraped_job_postings (for job in scraped_job_postings:).
#Cross-Reference Data: Inside the loop, extract the "core_skill" from the current dictionary. Use an if statement with the in operator to check if that specific skill exists inside your global_unique_skills set from Day 15.
#Display System Output: If the skill matches, print: "[SKILL MATCH] Candidate profile aligns with {role} (ID: {job_id})".
scraped_job_postings=[
    {"job_id": 5001, "role": "Data Analyst", "core_skill": "SQL"},
    {"job_id": 5002, "role": "Backend Dev", "core_skill": "Java"},
    {"job_id": 5003, "role": "BI Developer", "core_skill": "PowerBI"}
]
print("--- DAY 16: JOB SKILL MATCHES ---")
for job in scraped_job_postings:
    job_id = job["job_id"]
    role = job["role"]
    core_skill = job["core_skill"]
    if core_skill in globla_unique_cells:
        print(f"[SKILL MATCH] Candidate profile aligns with {role} (ID: {job_id})")
print("\n")

# DAY-17

# Task of Day-17/Day-270

# Create a list named production_live_feed holding three structured rows with incomplete information:
#production_live_feed = [
 #   {"job_id": 7001, "role": "Data Scientist", "salary": 1200000, "location": "Hyderabad"},
  #  {"job_id": 7002, "role": "ML Engineer", "location": "Bangalore"}, # Missing salary
   # {"job_id": 7003, "role": "AI Researcher"} # Missing salary AND location
#]
#Build the Safe Extraction Engine: Write a for loop to iterate through production_live_feed.
#Extract Fields with Guardrails: * Extract role directly.
#Extract salary using .get() with a fallback integer default of 0.
#Extract location using .get() with a fallback string default of "Alternative / Remote".
#Display Cleaned Logs: Print a clean visual header line --- DAY 17: FAULT-TOLERANT PIPELINE --- and log each processed entry clearly to prove the pipeline ran smoothly across incomplete inputs without crashing

production_live_feed = [
    {"job_id": 7001, "role": "Data Scientist", "salary": 1200000, "location": "Hyderabad"},
    {"job_id": 7002, "role": "ML Engineer", "location": "Bangalore"}, # Missing salary
    {"job_id": 7003, "role": "AI Researcher"} # Missing salary AND location
]
print("--- DAY 17: FAULT-TOLERANT PIPELINE ---")
for production in production_live_feed:
    job_id=production["job_id"]
    job_role=production["role"]
    job_salary=production.get("salary",0)
    job_location=production.get("location","Alternative/Remote")
    print(f" Job ID: {job_id} | Job role : {job_role} | Job salary : {job_salary} | Job Location : {job_location} ")

