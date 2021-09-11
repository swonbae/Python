#

import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
cat
mat
pat
bat
'''

sentence = 'Start a sentence and then bring it to an end'

# print('\tTab')
# print(r'\tTab')

# pattern = re.compile(r'abc')
# pattern = re.compile(r'cba')
# pattern = re.compile(r'.')
# pattern = re.compile(r'\.')
# pattern = re.compile(r'coreyms\.com')
# pattern = re.compile(r'\d')
# pattern = re.compile(r'\W')
# pattern = re.compile(r'\s')
# pattern = re.compile(r'\bHa')     # when 'Ha' starts a word (a space before 'Ha')
# pattern = re.compile(r'\BHa')     # (no space before 'Ha')

# pattern = re.compile(r'\d{3}.\d{3}.\d{4}')            # phone numbers
# pattern = re.compile(r'\d{3}[-.]\d{3}[-.]\d{4}')      # phone numbers (only - or . between numbers)
# pattern = re.compile(r'[89]00[-.]\d{3}[-.]\d{4}')     # phone numbers starting with 800 or 900 

# pattern = re.compile(r'[1-5]')
# pattern = re.compile(r'[^a-zA-Z]')
# pattern = re.compile(r'[^b]at')
# pattern = re.compile(r'Mr\.?\s[A-Z]\w*')              # Mr. name or Mr name
# pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')         # Mr Ms Mrs
# pattern = re.compile(r'(Mr|Ms|Mrs)\.?(\s[A-Z]\w*)')

# # matches = pattern.finditer(text_to_search)        # returns match objects with extra information
# matches = pattern.findall(text_to_search)           # returns that matches in group(s) as a list of strings or tuples

# for match in matches:
#     print(match)


# with open('data.txt', 'r', encoding='utf-8') as f:
#     contents = f.read()
    
#     matches = pattern.finditer(contents)
    
#     for match in matches:
#         print(match)


# pattern = re.compile(r'^Start')     # match
# pattern = re.compile(r'^a')         # no match
# pattern = re.compile(r'end$')       # match
# pattern = re.compile(r'a$')         # no match

# matches = pattern.finditer(sentence)

# pattern = re.compile(r'sentence')
pattern = re.compile(r'start', re.IGNORECASE)   # re.IGNORECASE == re.I

# matches = pattern.match(sentence)       # checks for a match only at the beginning of the string
matches = pattern.search(sentence)        # search entire string

print(matches)

# for match in matches:
#     print(match)

# print(text_to_search[1:4])    # 'abc'