#1
import re

pattern = r'a(b*)'

test_strings = list(map(str,input().split()))


for string in test_strings:
    match = re.search(pattern, string)
    if match:
        print(f"{string} matches the pattern '{pattern}'")
    else:
        print(f"{string} does not match the pattern '{pattern}'")



#2
import re

pattern = r'a(b{2,3})'

test_strings = list(map(str,input().split()))

for test_string in test_strings:
    match = re.search(pattern, test_string)
    if match:
        print(f"{test_string} matches the pattern")
    else:
        print(f"{test_string} does not match the pattern")

#3
import re

pattern = r'[a-z]+_[a-z]+'

txt = str(input())

matches = re.findall(pattern, txt)

print(matches)


#4

import re

pattern = r'[A-Z][a-z]+'

test_string = str(input())

matches = re.findall(pattern, test_string)

print(matches)

#5

import re

pattern = r'a.*b$'

test_strings = ['acb', 'a1234b', 'a_b', 'ab', 'acbb']

for test_string in test_strings:
    match = re.search(pattern, test_string)
    if match:
        print(f"{test_string} matches the pattern")
    else:
        print(f"{test_string} does not match the pattern")


#6
        
import re

pattern = r'[ ,.]'

test_string = 'Hello, world. How are you?'

new_string = re.sub(pattern, ':', test_string)

print(new_string)


#7

def snake_to_camel(snake_str):
    words = snake_str.split('_')
    
    camel_words = [words[0]] + [word.capitalize() for word in words[1:]]
    
    camel_str = ''.join(camel_words)
    
    return camel_str

snake_str = 'hello_world_how_are_you'
camel_str = snake_to_camel(snake_str)
print(camel_str)


#8

import re

pattern = r'[A-Z][^A-Z]*'

test_string = 'HelloWorldHowAreYou'

split_list = re.findall(pattern, test_string)

print(split_list)

#9


def insert_spaces(s):
    result = ''
    for i, c in enumerate(s):
        if c.isupper() and (i > 0 and s[i-1].islower() or i > 1 and s[i-2:i].isspace()):
            result += ' '
        result += c
    return result

s = 'HelloWorldHowAreYou'
new_s = insert_spaces(s)
print(new_s)


#10


def camel_to_snake(s):
    result = ''
    for c in s:
        if c.isupper():
            result += '_' + c.lower()
        else:
            result += c
    return result

s = 'HelloWorldHowAreYou'
new_s = camel_to_snake(s)
print(new_s)