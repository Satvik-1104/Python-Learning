#Slicing
#Indexing - [ start : end : step ]

name = 'Vadisetti Pranay Satvik Reddy'

print(len(name))
print(name.find(' '))
surname = name[:9]
print(surname)
print(name.find('R'))
caste = name[24:]
print(caste)
funky_name = name[::2]
print(funky_name)
rev_name = name[::-1]
print(rev_name)

#Slicing - using slice function
# slice(start, end, step) - indexes can be positive/negative/mixed

google = 'http://google.com'
facebook = 'http://facebook.com'
instagram = 'http://instagram.com'

slice = slice(7, -4)
print(google[slice])
print(facebook[slice])