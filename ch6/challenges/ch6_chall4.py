
lst = "Where now?Who now?When now?".split("?")
print(lst) # ['Where now', 'Who now', 'When now', '']
# get rid of the trailing empty string element
lst.pop()
print(lst)