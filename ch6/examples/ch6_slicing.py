fict = [" Tolstoy", "Camus", "Orwell", "Huxley", "Austin"]
# get first three
print(fict[0:3])

# slicing a string
ivan = ("In place of death there\n"
        "was light.")
str_len = len(ivan)
print(ivan[0:17],ivan[17:str_len])

#[:] to make a shallow copy

copy_ivan = ivan[:]
print("\n",copy_ivan)

# negative index to look up items right to left
print(ivan[-1]) # '.'

