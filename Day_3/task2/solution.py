"""
Task 2: 
- Read and understand what are Regular expressions and 
how they evaluate.
- It is really important to understand how they evaluate else a 
bad regex can take down your systems. 
- Read about backtracking in REGEX evaluation.
"""
import re 
print("\tTab")

#raw string interpret the string as a literal string 
#so ita print \t also
print(r"\tTab")
#====================================================#
#                   re.compile()                     #
#====================================================#
pattern=re.compile(r'Pa8ern')
result_1 =pattern.findall('\tPa8ern: This is a Pa8ern')
print(result_1)
result_2=pattern.findall('Pa8ern:1 , Pa8ern:2, Pa8ern:3')
print(result_2)

#====================================================#
#                   finditer()                     #
#====================================================#
found = pattern.finditer("Pa8ern")
for finally_matched in found:
    print(finally_matched)


