# Slice the string "It was a bright cold day in April, and the clocks were striking thirteen." to include only the
# characters before the comma

txt = "It was a bright cold day in April, and the clocks were striking thirteen."

# My solution: split and grab first element
print(txt.split(",")[0])

# solution from GitHub
print("\n *** Start official solution w mods ***\n")
sentence = "It was a bright cold day in April, and the clocks were striking thirteen."
slce = sentence[0:33]
print(slce)

# I don't quite agree w the given solution's slicing to the comma. How was [0:33] arrived at? Manual counting?
# seems better to get the index of the comma and use that

slce_idx = sentence.index(",")
print("The slice index of the comma is {}".format(slce_idx))
slce = sentence[0:slce_idx]
print(slce)
