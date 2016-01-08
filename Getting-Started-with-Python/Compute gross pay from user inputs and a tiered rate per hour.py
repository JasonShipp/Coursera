'''
Write a program to prompt the user for hours and rate per hour, and compute gross pay when the rate per hour increases after 40 hours. 
'''

hrs = raw_input("Enter Hours:")
h = float(hrs)

rph = float(raw_input('Enter Rate Per Hour:'))

if h <= 40:
    pay = h * rph
else:
    pay = (40 * rph) + ((h-40)*(1.5 * rph))
    
print pay
