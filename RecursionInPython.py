#recursive function to calculate factorial
#n! = n*(n-1)!
def fact(n):
    if n == 1:
        return 1
    elif n > 1:
        return n*(fact(n-1))
print(fact(5))