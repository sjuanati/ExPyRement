r"""
regular expressions (regex):
. : anything: letters, numbers, symbols... but no newlines
+ : one or more of
* : zero or more of
? : zero or one of
\ has to be put in front of any non regex symbol

[abc] : matches anything containing a, b or c
[a-z] : matches any letter (in lower case)
[A-z] : matches any letter (both upper & lower case)

regex editor : https://regexr.com/
"""

import re


def test():
    email = "marc.horse@hotmail.com"
    
    expression = r"[a-z]+"
    matches = re.findall(expression, email)
    print(matches)  # Output: ['marc', 'horse', 'hotmail', 'com']

    expression = r"[a-z\.]+"
    matches = re.findall(expression, email)
    print(matches) # Output: ['marc.horse', 'hotmail.com']

    price = 'Price: $1,267,896.50'
    expression = 'Price: \$([0-9,]*\.[0-9]*)'
    matches = re.search(expression, price)
    print(matches.group(0)) # Output: Price: $1,267,896.50 (entire match)
    print(matches.group(1)) # Output: 1,267,896.50 (first thing in brackets)
    price_without_comma = matches.group(1).replace(',', '')
    price_number = float(price_without_comma)
    print(price_number) # Output: 1267896.5