#First-last
#Take a sequence (str, list or tuple), and return the first and last elements, in a two element sequence OF THE SAME TYPE.

def first_last(sequence):
    return sequence[:1] + sequence[-1:]

print(first_last(['a','n','b','m']))
print(first_last(('a','n','b','m')))
print(first_last('anbm'))

#Create a function that takes a list or tuple of numbers, returning a two element list that sums even index numbers and odd 
#index numbers

def even_odd(sequence):
    new_list = [0,0]
    for index,number in enumerate(sequence):
        if index % 2 == 0:
            new_list[0] += number
        else:
            new_list[1] += number
    return new_list


print(even_odd([10,20,30,40,50,60]))

#Create a function that takes a list or tuple of numbers, returning the result of alternatively adding or subtracting numbers
#in the list or tuple

def plus_minus(sequence):
    total = sequence[0]
    for index,number in enumerate(sequence[1:]):
        if index % 2 == 0:
            total += number
        else:
            total -= number
    return total


print(plus_minus([10,20,30,40,50,60]))