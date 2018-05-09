''' PROBLEM: You need to unpack N elements from an iterable, 
    but the iterable may be longer than N elements, causing a 
    “too many values to unpack” exception. '''

''' example #1 '''

record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print('Name: {}'.format(name))
print('Email: {}'.format(email))
print('Phone Numbers: {}'.format(phone_numbers))

''' example #2 '''

records = [
     ('foo', 1, 2),
     ('bar', 'hello'),
     ('foo', 3, 4),
]

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)
