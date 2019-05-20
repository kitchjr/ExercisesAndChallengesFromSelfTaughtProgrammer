# take this list [" The", "fox", "jumped", "over", "the", "fence", "."] and turn it into a grammatically correct string.
# There should be a space between each word, but no space between the word 'fence' and the period that follows it.

txt = [" The", "fox", "jumped", "over", "the", "fence", "."]
join_txt = " ".join(txt)
print(join_txt)  # The fox jumped over the fence .
# fix period at the end
join_txt = join_txt[0:-2] + "."
print(join_txt)
