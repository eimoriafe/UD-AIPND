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

text_outgoing_incoming = []
for i in texts:
    text_outgoing_incoming.extend(i[0:2])
unique_text_num = set(text_outgoing_incoming)

calls_incoming = set()
calls_outgoing = set()
for i in calls:
    calls_incoming.add(i[1])
    calls_outgoing.add(i[0])

unique_telemarketers = sorted(calls_outgoing - calls_incoming - unique_text_num)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
print("These numbers could be telemarketers:")
print('\n'.join(map(str, unique_telemarketers)))
