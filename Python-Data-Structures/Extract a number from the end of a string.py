'''
Write a program to extract the number at the end of the text below, using find() and string slicing.
'''

text = "X-DSPAM-Confidence:    0.8475"

print float(text[text.find('0'):len(text)+1])
