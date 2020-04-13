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

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

longest_caller = ''
longest_call_time = 0
time_spent_dict = {}
for entry in calls:
    if entry[0] in time_spent_dict:
        time_spent_dict[entry[0]] += int(entry[3])
    else:
        time_spent_dict[entry[0]] = int(entry[3])
    if entry[1] in time_spent_dict:
        time_spent_dict[entry[1]] += int(entry[3])
    else:
        time_spent_dict[entry[1]] = int(entry[3])
    
for key, value in time_spent_dict.items():
    if value > longest_call_time:
        longest_call_time = value
        longest_caller = key

print(longest_caller) 
print(longest_call_time)

print("{telephone_number} spent the longest time, {total_time} seconds, on the phone during September 2016.".format(telephone_number = longest_caller, total_time = longest_call_time))
