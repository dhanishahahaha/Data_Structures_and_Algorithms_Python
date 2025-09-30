'''Regular expressions

--> A regular expression is a special string pattern that describes how to search for or match text.
--> Normal text: looks for exact characters ("abc" matches only "abc").
--> Regex: uses symbols and rules to match patterns (e.g., "a.c" matches "abc", "axc", "a1c", etc.).

--> Regex is Case sensitive.
--> Methods to find matches  1.finditer 2.findall 3.match() 4.search()

'''
#1. finditer() - returns the matched text span,start and end. 
#matches = pattern.finditer(r"abc",test_string)
import re

test_string = "123abc456789abc123ABC"
pattern = re.compile(r"abc")  #r--> makes it the raw string
matches = pattern.finditer(test_string)  #1. we can also directly so finditer without compiling first
#matches = pattern.finditer(r"abc",test_string)

for match in matches:
    print(match)
    print(match.span() , match.start() , match.end()) #gives the span,start and end


#2. findall() - gives you the matched text
test_string = "123abc456789abc123ABC"
pattern=re.compile(r"abc")
matches = pattern.findall(test_string) 

for match in matches:
    print(match)


#3. match() - returns an output if it matches at the beginning of the string.
test_string = "123abc456789abc123ABC"
pattern=re.compile(r"abc")
match = pattern.match(test_string) 

print(match)  #returns None because abc not at the beginning. 


#4. search() - searches for the first match in the string.
test_string = "123abc456789abc123ABC"
pattern=re.compile(r"abc")
matches = pattern.search(test_string) 

print(matches)