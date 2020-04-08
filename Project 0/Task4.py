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

#Solution:
called_by_telemarketers = set()

for entry in calls:
  if "140" in entry[0]:
      if entry[0][0:3] == '140':
        called_by_telemarketers.add(entry[0])

print("These numbers could be telemarketers: ")
print(*sorted(called_by_telemarketers), sep = "\n")
