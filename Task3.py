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

called_by_080 = set()
for i in calls:
    if '(080)' in i[1]:
        called_by_080.add(i[0])

fc = set()
for y in called_by_080:
    if y.startswith('7') or y.startswith('8') or y.startswith('9'):
        fc.add(y[0:4])
    elif y.startswith('140'):
        fc.add(y[0:3])
    else:
        fc.add(y[0:(y.index(')') + 1)])

sc = sorted(fc)

m080 = []
for i in calls:
    if '(080)' in i[0]:
        if '(080)' in i[1]:
            m080.append(i[0:2])

col_080 = []
for i in calls:
    if '(080)' in i[0]:
        col_080.append(i[0])

match_percent = (len(m080) / len(col_080)) * 100
"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.
"""
print("The numbers called by people in Bangalore have codes:")
print("\n".join(map(str, sc)))

"""
Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format("%.2f" % match_percent))
