"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

caller_col_with_dur = []
receiver_col_with_dur = []
for i in calls:
    caller_col_with_dur.append(i[0:4:3])
    receiver_col_with_dur.append(i[1:4:2])

agg_call_dic = dict()
for num_elements in caller_col_with_dur:
    if num_elements[0] in agg_call_dic:
        agg_call_dic[num_elements[0]] += int(num_elements[1])
    else:
        agg_call_dic[num_elements[0]] = int(num_elements[1])

agg_receiver_dic = dict()
for num_elements in receiver_col_with_dur:
    if num_elements[0] in agg_receiver_dic:
        agg_receiver_dic[num_elements[0]] += int(num_elements[1])
    else:
        agg_receiver_dic[num_elements[0]] = int(num_elements[1])

agg_sum = {**agg_call_dic, **agg_receiver_dic}
for key,value in agg_sum.items():
    if key in agg_call_dic and key in agg_receiver_dic:
        agg_sum[key] = (agg_call_dic[key] + agg_receiver_dic[key])

key_max = max(agg_sum.keys(), key=(lambda k: agg_sum[k]))
"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
print("{} spent the longest time, {} seconds, on the phone during September 2016".format(key_max, agg_sum[key_max]))
