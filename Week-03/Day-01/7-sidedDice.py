import random

def rand5():
    return random.randint(1, 5)

def rand7():

    # Implement rand7() using rand5()
    while True:
        first = 5 * (rand5() - 1)
        second = rand5()
        total = first + second
        if total <= 21:
            return total % 7 + 1

print 'Rolling 7-sided die...'
print rand7()
print

print 'Rolling 7-sided die...'
print rand7()
print

print 'Rolling 7-sided die...'
print rand7()
print

print 'Rolling 7-sided die...'
print rand7()
print