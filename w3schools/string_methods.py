# String methods

# Note: All string methods return new values.
# They do not change the original value.

txt: str = "the bOok name is BLUE"

# Capitalize * Not title() *

print(txt.capitalize()) # Output: The book name is blue

# Casefold 

print(txt.casefold()) # Output: the book name is blue
# Similar to lower() but aggressive


# Center

txt: str = "Middleman"

print(txt.center(20)) # Output:      Middleman      
print(txt.center(20, "-")) # Output: -----Middleman------

# Count

txt: str = "Blue is everywhere, Why Blue is so common? My face is even Blue."

print(txt.count("Blue")) # Output: 3
print(txt.count("Blue", 10)) # Output: 2
print(txt.count("Blue", 10, 30)) # Output: 1

# Encode

txt: str = "My name is Ský"

print(txt.encode(encoding="ascii",errors="backslashreplace")) # Output: b'My name is Sk\\xfd' 
print(txt.encode(encoding="ascii",errors="ignore")) # Output: b'My name is Sk'
print(txt.encode(encoding="ascii",errors="namereplace")) # Output: b'My name is Sk\\N{LATIN SMALL LETTER Y WITH ACUTE}'
print(txt.encode(encoding="ascii",errors="replace")) # Output: b'My name is Sk?'
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace")) # Output: b'My name is Sk&#253;'

# Endswith

txt: str = "Being empty is better than being drunk."

print(txt.endswith(".")) # Output: True
# Syntax: string.endswith(value, start, end)

# Expand tabs

txt: str = "H\te\tl\tl\to"

print(txt) # Output: H 	   e	   l	   l    	o
print(txt.expandtabs()) # Output: H 	   e	   l	   l    	o
# Same as regular because default tabsize is 8

print(txt.expandtabs()) # Output: H e l l o

# Find

txt: str = "Do not lose hope nor be sad."

print(txt.find("hope")) # Output: 12
# Syntax: string.find(value, start, end)

print(txt.find("happyness")) # -1
# Unlike index() it doesn't raise an exception



