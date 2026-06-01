# DAY-15

# Task

# Create this mock database structure: dataset = [[10, 20], [30, 40], [50, 60]].
#Write an outer loop using enumerate() to track the row index: for row_index, row_data in enumerate(dataset):
#Write an inner loop to process the items inside row_data.
#Print an f-string that clearly states the location of the data point: "Found value {item} in Row {row_index}".

dataset=[[10, 20], [30, 40], [50, 60]]
for row_index,row_data in enumerate(dataset):
    for c in row_data:
        print(f"Found value {c} in Row {row_index}")