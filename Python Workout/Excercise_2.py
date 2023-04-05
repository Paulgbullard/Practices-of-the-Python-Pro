#Create a function to replicate the functionality of sum()

def mysum(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(mysum(1,2,3))

#Create a second function that has a starting point for the sum to begin from

def mynewsum(starting_point,*numbers):
    total = starting_point
    for num in numbers:
        total += num
    return total

print(mynewsum(10, 1,2,5))

#Create a third function to find the mean

def mymean(*numbers):
    total = 0
    count = 0
    for num in numbers:
        total += num
        count += 1
    total = total / count
    return total

print(mymean(1,2,3))
