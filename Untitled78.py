#!/usr/bin/env python
# coding: utf-8

# Q1. What is the benefit of regular expressions?
# 

# Regular expressions provide a powerful and flexible way to work with text, enabling you to perform complex operations with minimal code.

# Q2. Describe the difference between the effects of "(ab)c+" and "a(bc)+." Which of these, if any, is the unqualified pattern "abc+"?
# 

# "(ab)c+" matches strings starting with "ab" followed by one or more "c" characters.
# 
# "a(bc)+" matches strings starting with "a" followed by one or more occurrences of "bc".
# 
# The unqualified pattern "abc+" matches strings starting with "abc" followed by one or more "c" characters.
# 

#  How much do you need to use the following sentence while using regular expressions?
# 
# 
# 
# import re
# 

# "import re" is used in Python to import the re module for working with regular expressions.

# Q4. Which characters have special significance in square brackets when expressing a range, and under what circumstances?
# 

# The hyphen (-) is used to define a character range.
# The caret (^) negates the character set if it appears as the first character.
# Other characters are generally treated literally within square brackets.

# Q5. How does compiling a regular-expression object benefit you?
# 

# Improved performance: The compiled object can be reused, leading to faster execution.
# Readable and maintainable code: Assigning a descriptive name enhances code readability and makes it easier to modify.
# Optimization options: Additional flags can be used to control matching behavior.
# Advanced features: Compiled objects often provide access to advanced methods for more powerful text processing.

# Q6. What are some examples of how to use the match object returned by re.match and re.search?
# 

# In[6]:


import re
pattern = r'\d+'
text = "the match price is $20"

match = re.search(pattern, text)
if match:
    matched_string = match.group()
    print("matched string:" , matched_string)
    print("start position:" , match.start())
    print("End position:" , match.end())


# Q7. What is the difference between using a vertical bar (|) as an alteration and using square brackets as a character set?
# 

#  The vertical bar (|) is used for alternation between multiple patterns, while square brackets ([]) are used to define a character set for matching any single character from that set.
# 
# 
# 
# 
# 

# Q8. In regular-expression search patterns, why is it necessary to use the raw-string indicator (r)? In   replacement strings?
# 

# The raw-string indicator (r) is used in regular expressions to treat the string as a raw string, interpreting backslashes literally. This avoids conflicts between regular expression syntax and Python string literal syntax. It simplifies writing regular expressions by eliminating the need for double-escaping special characters.

# In[ ]:




