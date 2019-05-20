# get index of the first occurence of a character in a string w the index method
print("animals".index("m")) # 3

# use exception handling if not sure a match will be found

try:
    print("animals".index("z"))
except:
    print("Not found")