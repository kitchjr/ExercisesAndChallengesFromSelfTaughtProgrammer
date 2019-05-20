# separating a string into two or more strings
# split takes place on the given parameter

txt = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness,\
it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness,\
it was the spring of hope, it was the winter of despair …, we had nothing before us, we were all going direct to\
Heaven, we were all going direct the other way..."

# split by comma
split_text = txt.split(",")
print(split_text)
