'''
Write a program to prompt the user for a score between 0.0 and 1.0, and compute a grade from this score.
'''

score = float(raw_input('Enter score between 0 and 1:'))
    
if score >= 0 and score <= 1:
    
    if score < 0.6:
        grade = 'F'
    elif score >= 0.9:
        grade = 'A'
    elif score >= 0.8:
        grade = 'B'
    elif score >= 0.7:
        grade = 'C'
    elif score >= 0.6:
        grade = 'D'
    
    print grade
    
else:
    print 'Score is not between 0 and 1; please try again'    
