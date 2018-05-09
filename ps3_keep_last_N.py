'''PROBLEM: You want to keep a limited history of the last few items 
seen during iteration or during some other kind of processing.'''

''' example 1 '''

from collections import deque

q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print ('q: {}'.format(q))
q.append(4)
print ('q: {}'.format(q))
q.append(5)
print ('q: {}'.format(q))
q.appendleft(6)
print ('q: {}'.format(q))
q.pop()
print ('q: {}'.format(q))
q.popleft()
print ('q: {}'.format(q))

'''Adding or popping items from either end of a queue has O(1) complexity. 
This is unlike a list where inserting or removing items from the front of the list is O(N).'''

''' example #2 '''

from collections import deque

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

if __name__ == '__main__':
    with open('somefile.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-'*20)
