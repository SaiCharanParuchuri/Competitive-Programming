import random

def rand7():
    return random.randint(1, 7)

def rand5():

    # Implement rand5() using rand7()
    # a=rand7()
    # print a
    # if a<6:
    #     return a
    # return rand5()
    # print i=rand7()
    while True:
        i=rand7()
        if i<6:
            return i

print 'Rolling 5-sided die...'
print rand5()
print

print 'Rolling 5-sided die...'
print rand5()
print

print 'Rolling 5-sided die...'
print rand5()
print

print 'Rolling 5-sided die...'
print rand5()
print

