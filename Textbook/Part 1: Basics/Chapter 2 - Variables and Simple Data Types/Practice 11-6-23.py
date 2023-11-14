#2-3 - Use a variable to represent a person's name, and print a message ot that person. Your message should be simple, such as, "Hello Eric, would you like to learn some Python today"
name = "eric"
print(f"Hello {name.title()}, would you like to learn some Python today?")

#2-4 Use a veriable to represent a person's name, and then print that person's name in lowercase, uppercase, and title case.
name2 = "jamie"
print(f"\n{name2.title()}\n{name2.upper()}\n{name2.lower()}")

#2-5 Find a quote froma  famouse person you admire. Print the quote and the name of it's aurthor.
name3 = "david goggins"
name4 = "jordan peterson"
print(f"{name3.title()} and {name4.title()} share similar sintements in that they both beleive life is suffering.")

#2-6 Repeat exercise 2-5, but this time, represent the famous person's name using a varibale called fmaous_person. then compose your message and represent it with a new variable called message. Print your message.
famouse_person = "jocko willink"
message = " most certainly belives that we must do the hard thing, for the hard thing bares the greatest fruit. No step forward is too small"
print(famouse_person.title(), message)

#2-7 Use a veriable to represent a person's name, and invlude some whitespace characters at the beggening and end of the name. Make sure yuou use each character combination, "\t and "\n, at least once.
#Then pring the name using each of the three stripping functions, lstrip(), rstrip(), and strip().
famouse_person2 = " kanye west "
print(famouse_person.title())
print(f"\n{famouse_person2.title().lstrip()}")
print(f"\n\t{famouse_person2.title().rstrip()}")
print(f"\n{famouse_person2.title().strip()}")