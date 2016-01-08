'''
Write a program that repeatedly prompts the user for integer numbers until the user enters 'done'.
Once 'done' is entered, print out the largest and smallest of the numbers.
'''

largest = None
smallest = None

while True:
    num = raw_input("Enter a number: ")
    if num == "done": break
    try:
        int(num)
        if largest == None:
            largest = num
        else:
            if num > largest:
                largest = num
        
        if smallest == None:
            smallest = num
        else:
            if num < smallest:
                smallest = num
    except:
        print 'Invalid input'
    

print "Maximum is", largest
print "Minimum is", smallest
