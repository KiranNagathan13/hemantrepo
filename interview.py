#(1)----------------------------------
# get the key which has maximum value in a dictionary
#(i)----------------------------------
d = {'a': 1, 'b':2, 'c':3, 'd':4}
v = 0
for key, value in d.items():
    if value > v:
        v = value
for key in d.keys():
    if d[key] == v:
        print(key)

#(ii)----------------------------------
for key, value in d.items():
    if max(d.values()) == value:
        print(key)

#(2)-----------------------------------
# check whether character is a consonent or not
import re

if re.findall(r"[^aeiou]", "e"):
    print("its a consonent")
else:
    print("its a vowel")

