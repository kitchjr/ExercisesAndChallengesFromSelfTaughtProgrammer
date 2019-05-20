# The format method is useful if you are creating a string from user input like in this mini mad lib
noun1 = input("Enter a noun:")
verb = input("Enter a verb:")
adjective = input("Enter an adjective:")
noun2 = input("Enter a noun:")

r = """The {} {} the {} {}""".format(noun1, verb, adjective, noun2)

print(r)
