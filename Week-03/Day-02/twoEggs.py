import math
def my_function(floors):

    # Write the body of your function here
    temp = math.sqrt(1+(8*floors))
    high = (-1+temp)/2
    low = (-1-temp)/2
    return 'For %s floors, the highest floor is %s' % (floors, math.ceil(max(high,low)))

# Run your function through some test cases here
# Remember: debugging is half the battle!
print my_function(floors=100)

print my_function(floors=200)

print my_function(floors=300)

print my_function(floors=400)

print my_function(floors=500)