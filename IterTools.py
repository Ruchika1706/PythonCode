#set of tools for functional programming
#standard library which contains functions useful for functional programming
#import itertools or from itertools import count
#count function will count from a  given number till infinity
from itertools import count,takewhile
for i in count(3):
    print(i)
    if i >= 20:
        break
numbers = [1,2,3,4,5,6,7,8,8]
#takewhile function
#takewhile first argument is predicate, second is iterable on which the predicate is true, those elemtns are printed.
print(list(takewhile(lambda x: x<=6,numbers)))





    