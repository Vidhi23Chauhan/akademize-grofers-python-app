content = open("dummy-data.csv", "r").read()
lines = content.split("\n")

# Extracting the header row
header_row = lines[0].split(",")

# extracting the record rows
lines = lines[1:]

# count of rows
print(header_row)
print(lines)
print(len(header_row))
print(len(lines))

"""
['item_id', 'is_p_off', 'is_p_off', 'is_flat_p', 'd_value', 'start_date', 'end_date']

['1,0,1,1,410,20/04/21 15:20,26/04/21 23:59', '2,0,1,0,361,20/04/21 15:20,26/04/21 23:59', '3,1,1,1,19,20/04/21 15:20,26/04/21 23:59', '4,1,1,1,57,20/04/21 15:20,26/04/21 23:59', '5,1,0,0,190,20/04/21 15:20,26/04/21 23:59', '6,1,0,1,189,20/04/21 15:20,26/04/21 23:59', '7,0,0,1,94,20/04/21 15:20,26/04/21 23:59', '8,0,0,0,299,20/04/21 15:20,26/04/21 23:59', '9,0,1,1,427,20/04/21 15:20,26/04/21 23:59', '10,0,1,1,370,20/04/21 15:20,26/04/21 23:59']

7
10

"""

# Preparing a multi dimensional array - records
records = []
count = 0
for line in lines:
    cells = line.split(",")
    cells = cells[:5]  # keeping only the first 5 cells
    records.append(cells)

# Printing the first 5 records
for record in records[:5]:
    print(record)

"""
[
    ['1', '0', '1', '1', '410'],
    ['2', '0', '1', '0', '361'],
    ['3', '1', '1', '1', '19'],
    ['4', '1', '1', '1', '57'],
    ['5', '1', '0', '0', '190']
]
"""

"""
Doubt

# Printing the 4th and 5th value of 5 records of lines
print(record[4][3])
print(record[4][4])

giving an error
IndexError: string index out of range

"""

# Summing up the 5th column values
sum = 0
for record in records[:5]:
    sum += int(record[4])

print(f"Sum of {header_row[4]} = {sum}")

"""
Sum of d_value = 1037

"""

# Filtering out the records with 4th column value = 0
filtered_records = []
for record in records:
    is_flat_d = int(record[3])
    if is_flat_d == 0:
        filtered_records.append(record)

print("Filtered records:")
for record in filtered_records:
    print(record)

"""
Filtered records:
['2', '0', '1', '0', '361']
['5', '1', '0', '0', '190']
['8', '0', '0', '0', '299']

"""

# Extract required columns 0 and 1 (Item Id and d_value)
new_record_set = [
    ["item_id", "d_value"]
]
for record in records:
    item_id = record[0]
    d_value = record[4]
    new_record = [item_id, d_value]
    new_record_set.append(new_record)

print("First 5 records in new record set:")
for record in new_record_set[:5]:
    print(record)

"""

First 5 records in new record set:
['item_id', 'd_value']
['1', '410']
['2', '361']
['3', '19']
['4', '57']

"""


# Prepare a string of csv
new_record_lines = []
for record in new_record_set:
    new_record_lines.append(",".join(record))

print("Joined first 5 records in new record set by ',':")
for record in new_record_lines[:5]:
    print(record)

"""

Joined first 5 records in new record set by ',':
item_id,d_value
1,410
2,361
3,19
4,57

"""

new_records_content = "\n".join(new_record_lines)
f = open("out_put.csv", "w")
f.write(new_records_content)
print("New record set has been written to out_put.csv")

