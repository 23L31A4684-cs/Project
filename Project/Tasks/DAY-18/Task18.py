# DAY-18

# Task

# Create a dataset tracking processing metrics:
#Write a single line of code to sort server_logs by "duration_sec" in descending order (slowest process first) and save it to a variable named ranked_logs.
#Write a for loop to step through ranked_logs and print out an f-string summary: f"[SLOW PROCESS RANKING]: Process {row['process_id']} took {row['duration_sec']} seconds."

server_logs = [
    {"process_id": "P-10", "duration_sec": 4.5},
    {"process_id": "P-11", "duration_sec": 1.2},
    {"process_id": "P-12", "duration_sec": 8.9}
]
ranked_logs=sorted(server_logs,key=lambda c:c["duration_sec"],reverse=True)
print(ranked_logs)
for k in ranked_logs:
    print(f"[SLOW PROCESS RANKING]: Process {k['process_id']} took {k['duration_sec']} seconds.")