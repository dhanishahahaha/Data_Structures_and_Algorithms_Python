'''Regular expressions

--> A regular expression is a special string pattern that describes how to search for or match text.
--> Normal text: looks for exact characters ("abc" matches only "abc").
--> Regex: uses symbols and rules to match patterns (e.g., "a.c" matches "abc", "axc", "a1c", etc.).

--> Regex is Case sensitive.
--> Methods to find matches  1.finditer 2.findall 3.match() 4.search()

--> All meta characters . ^ $ * + ? { } [ ] | ( ) \ | ()
    1. . any character
    2. ^ starts with "^hello"
    3. $ ends with "world$"
    4. * zero or more occurances "aix*"
    5. + one or more occurances "aix+"
    6. { } exactly the specified number of occurances "al{2}"
    7. [] a set of characters "[a-m]"
    8. \ special sequence or escape special characters "\d"
    9. | either or "falls|stays"
    10. ( ) capture and group

--> More special characters \d   \D   \w   \W   \s   \S   \b   \B   \A   \Z   \G
    1. \d : Matches any decimal digit [0-9]
    2. \D : Matches any non digit character 
    3. \s : Matches any whitespace character (" " , \t , \n)
    4. \S : Matches any non - whitespace character
    5. \w : Matches any alpha-numeric word [a-zA-Z0-9_]
    6. \W : Matches any non alpha-numeric word
    7. \b : Matches where the specified characters are at the beginning or the end of a word.
    8. \B : Matches where the specified characters are present, but not at the beginning

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

#meta characters
#1. . any character

test_string = "123abc456789abc123ABC"
pattern=re.compile(r".")
matches = pattern.finditer(test_string) 

for match in matches:
    print(match.group())

#2. ^ starts with 
test_string = "123abc456789abc123ABC"
pattern=re.compile(r"^123")
matches = pattern.finditer(test_string) 

for match in matches:
    print(match)

#3. $ ends with
test_string = "123abc456789abc123ABC"
pattern=re.compile(r"123$")
matches = pattern.finditer(test_string) 

for match in matches:
    print(match) #returns nothing because it doesnt end with 123

#special characters
#1. \d - for all digit num
import re
test_string = "hello 123 hello_ho hohey"
pattern=re.compile(r"\d")
matches = pattern.finditer(test_string) 

for match in matches:
    print(match) 

#2. \D - for non digit nums
test_string = "hello 123 hello_ho hohey"
pattern=re.compile(r"\D")
matches = pattern.finditer(test_string) 

for match in matches:
    print(match) 


#3. \s - for whitespace character
test_string = "hello 123 hello_ho hohey"
pattern=re.compile(r"\s")
matches = pattern.finditer(test_string) 

for match in matches:
    print(match) 


#4. \S - for non whitespace character
test_string = "hello 123 hello_ho hohey"
pattern=re.compile(r"\S")
matches = pattern.finditer(test_string) 

for match in matches:
    print(match) 


#5. \w - for alphanumeric character
test_string = "hello 123 hello_ho hohey"
pattern=re.compile(r"\w")
matches = pattern.finditer(test_string) 

for match in matches:
    print(match) 


#6. \W - for non alphanumeric character
test_string = "hello 123 hello_ho hohey"
pattern=re.compile(r"\W")
matches = pattern.finditer(test_string) 

for match in matches:
    print(match) 


#7. \b - for matching at the beginning of a string
test_string = "hello 123 hello_ho hohey"
pattern=re.compile(r"\bhello")
matches = pattern.finditer(test_string) 

for match in matches:
    print(match) 


#8. \B - for matching NOT at the beginning of a string
test_string = "hello 123 hello_ho hohey"
pattern=re.compile(r"\Bhey")
matches = pattern.finditer(test_string) 

for match in matches:
    print(match) 