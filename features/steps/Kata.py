# for lesson 4
"""Given a random non-negative number, you have to return t
  he digits of this number within an array in reverse order.
  Example:348597 => [7,9,5,8,4,3]
"""


def digitize(n):
    n = str(n)[::-1]
    arr = []
    for i in n:
        arr.append(int(i))
    return arr
print(digitize(1245678))


# 2 ways

def digitize_2(n):
    return [int (i) for i in str(n)[::-1]]
print(digitize_2(3457890))


# for lesson 5
"""Your fellow coders have bought you several drinks tonight in the form of a string. 
Return a string suggesting how many glasses of water you should drink to not be hungover.

Examples
"1 beer"  =>  "1 glass of water"
"1 shot, 5 beers and 1 glass of wine"  =>  "7 glasses of water

"""
def hydrate(drink_string):
    r = sum(int(i) for i in drink_string if i in '123456789')
    if r == 1:
        return '1 glass of water'
    return f'{r} glasses of water'

print(hydrate("5 beers"))
