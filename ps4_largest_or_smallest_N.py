'''PROBLEM: You want to make a list of the largest or smallest N items in a collection.'''

''' example #1 '''

import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))  # Prints [42, 37, 23]
print(heapq.nsmallest(3, nums)) # Prints [-4, 1, 2]

''' example #2 '''

import heapq

portfolio = [
             {'name': 'IBM', 'shares': 100, 'price': 91.1},
             {'name': 'AAPL', 'shares': 50, 'price': 543.22},
             {'name': 'FB', 'shares': 200, 'price': 21.09},
             {'name': 'HPQ', 'shares': 35, 'price': 31.75},
             {'name': 'YHOO', 'shares': 45, 'price': 16.35},
             {'name': 'ACME', 'shares': 75, 'price': 115.65}
            ]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
print('Cheap: {}'.format(cheap))
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
print('Expensive: {}'.format(expensive))

''' example #3 '''

import heapq

nums = (1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2)
h = list(nums)
heapq.heapify(h)        # converts a list to heap. argument must be a list
print('h: {}'.format(h))
heapq.heappop(h)        # pops the smallest element out of heap
print('h: {}'.format(h))
heapq.heappush(h,99)    # pushes the new element into heap
print('h: {}'.format(h))
heapq.heappushpop(h,1)  # pushes the new element first then pops smallest element 
print('h: {}'.format(h))
heapq.heapreplace(h,1)  # pops smallest element first then pushes the new element
print('h: {}'.format(h))

'''
    1. If N is about the same size as the collection itself, it is usually faster to 
    sort it first and take a slice (i.e., use sorted(items)[:N] or sorted(items)[-N:])
    2. The nlargest() and nsmallest() functions are most appropriate if you are trying 
    to find a relatively small number of items.
    3. If you are simply trying to find the single smallest or largest item (N=1), it 
    is faster to use min() and max().
'''
