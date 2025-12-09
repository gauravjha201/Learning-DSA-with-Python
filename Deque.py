from collections import deque

lst=deque([])

lst.append(3)
lst.append(2)
lst.appendleft(1)
lst.appendleft(0)
lst.pop()


print(lst)