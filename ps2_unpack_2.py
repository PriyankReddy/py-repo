''' PROBLEM: You need to unpack N elements from an iterable, 
    but the iterable may be longer than N elements, causing a 
    “too many values to unpack” exception. '''

''' example #1 '''

record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print('Name: {}'.format(name))
print('Email: {}'.format(email))
print('Phone Numbers: {}'.format(phone_numbers))
