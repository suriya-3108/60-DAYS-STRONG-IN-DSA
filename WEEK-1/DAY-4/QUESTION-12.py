"""
Question 12 (OrderedDict – Maintain Insertion Order)

Write a Python program to:
Create a dictionary with some key-value pairs:
data = {'apple': 3, 'banana': 2, 'cherry': 5}

Convert it into an OrderedDict
Add a new key-value pair 'date': 4
Print the OrderedDict

Expected output:
OrderedDict([('apple', 3), ('banana', 2), ('cherry', 5), ('date', 4)])

Rules / Notes:
Use collections.OrderedDict
Understand that OrderedDict preserves the insertion order (even though Python 3.7+ dict also preserves order)
Only basic usage is required
"""

from collections import OrderedDict

data = {'apple': 3, 'banana': 2, 'cherry': 5}

ordered_data = OrderedDict(data)

ordered_data['date'] = 4

print(ordered_data)
