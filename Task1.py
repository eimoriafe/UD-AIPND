"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

text_num_col1 = set()
text_num_col2 = set()
for x in texts:
    text_num_col1.add(x[0])
    text_num_col2.add(x[1])

text_num_col1.update(text_num_col2)

calls_rec_col1 = set()
calls_rec_col2 = set()
for y in calls:
    calls_rec_col1.add(y[0])
    calls_rec_col2.add(y[1])

calls_rec_col1.update(calls_rec_col2)
calls_rec_col1.update(text_num_col1)

unique_total = len(calls_rec_col1)
"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
print("There are "+str(unique_total)+" different telephone numbers in the records.")