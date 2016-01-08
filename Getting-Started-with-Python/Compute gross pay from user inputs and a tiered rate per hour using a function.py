'''
Write a program to prompt the user for hours and rate per hour, and feed these into a function. 
Use the function to compute gross pay when the rate per hour increases after 40 hours. 
'''

h = float(raw_input("Enter Hours:"))
rph = float(raw_input('Enter Rate Per Hour:'))

def computepay(h,rph):
    if h <= 40:
        pay = h * rph
    else:
        pay = (40*rph) + ((h - 40)*(rph * 1.5))
    return pay

p = computepay(h,rph)
print p
