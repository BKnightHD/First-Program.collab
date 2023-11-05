# -*- coding: utf-8 -*-
"""PythonCC.Chp3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bZm6qNWe4-NQoCFnnKH9wIiawwCQfJbh
"""

bicycles = ['trek', 'cannondale', 'redline', 'specialized'] #first list
print(bicycles)
#index positions start at 0, not 1
print("    " + bicycles[0].title())
print("\t" + bicycles[1].title())
print("\t\t" + bicycles[2].upper())
print("\t\t\t" + bicycles[3].title())
print(bicycles[-1], bicycles[-2])

message = "My first bicycle was a " + bicycles[2].title() + "."
print(message)

"""Try if yourself
* 3-1 Names
* 3-2 Greetings
* 3-3 Your Own List
"""

#3-1
names = ["Giuseppe", "Maisam", "Joe", "Devin", "Eddie"]
print(names[0],"\n",names[1],"\n",names[2],"\n",names[3],"\n",names[4])

#3-2
print("Hey " + names[0] + ", I hope you're having a great day!")
print("Hey " + names[1] + ", I hope you're having a great day!")
print("Hey " + names[2] + ", I hope you're having a great day!")
print("Hey " + names[3] + ", I hope you're having a great day!")
print("Hey " + names[4] + ", I hope you're having a great day!")

#3-3
stores = ['nordstroms', 'express', 'levis', 'north face', 'nike']
print("I use to go to West County mall all the time top shop at " + stores[-5].title())

motercycles = ['honda', 'yamaha', 'suzuki']
print(motercycles)

motercycles[0] = 'ducati' # here, we are changing the value stored in the first position of our motercycle list
print(motercycles)

motercycles = []
motercycles.append('honda')
motercycles.append('yamaha')
motercycles.append('suzuki')
print(motercycles)

motercycles = ['honda', 'yamaha', 'suzuki']
last_owned = motercycles.pop()
first_owned = motercycles.pop(0)


print(f"The first motercycle I owned was a {last_owned.title()}.") #inputing a varibale within a str without concatinating it, the f represents a "f-string"
print(f"The first motercycle I owned was a {first_owned.title()}.")

names = ['jeffery', 'tristan', 'jank', 'miles']
names.append('mason')
family = "jappa"
names.insert(0, 'maisam')
print("I'm praying for the " + str(family).title() + " family in there time of need.")
print("I hope this doesn't take my man " + names[-4].title() + " down the wrong path.")

"""Introducing the append and pop methods
* append() - adds a nother item to the list
* pop() - popping (or removing) the last item on the list
"""

colors = ['red', 'blue']
print(colors[1])

colors.append('green') # adding an item to the end of the list with the append method
print(colors)

popped_colors = colors.pop() # here, we are storing the value of the poped item into the variable named popped_colors
print(popped_colors)

colors.pop(1) # another way to pop an item form the list. Now the list only contains 1 item
print(colors)

motercycles = ['honda', 'yamaha', 'suzuki', 'ducanti']
print(motercycles)
motercycles.remove('honda') #remove function works well if you do not know the position of the item you want to delete
print(motercycles)

too_expensive = motercycles[1]
motercycles.remove(too_expensive)
print(motercycles)

print(f"\n{too_expensive.title()} is too expensive for me.")

"""Try it youreself
* 3-4 Guest List
* 3-5 Changing the Gues list
* 3-6 More Guests
* 3-7 Shrinking Guest List
"""

#3-4
invitations = ['Jesus Christ', 'sade', 'rayfield']

print(f"Hello {invitations[0].title()}, I'd like to formally invite you to dinner. It would be an honor to have you.")
print(f"Hello {invitations[1].title()}, I'd like to formally invite you to dinner. It would be an honor to have you.")
print(f"Hello {invitations[2].title()}, I'd like to formally invite you to dinner. It would be an honor to have you.")

#3-5
absent = invitations.pop(0)
invitations.insert(0,'mom') #insert function will add mom like append but I can now choose which position to add her
print(f"\nHello my honored guests, unfortunately {absent.title()} won't be joing us tonight.")
print(f"\nHello {invitations[0].title()}, I'd like to formally invite you to dinner. It would be an honor to have you.")
print(f"Hello {invitations[1].title()}, I'd like to formally invite you to dinner. It would be an honor to have you.")
print(f"Hello {invitations[2].title()}, I'd like to formally invite you to dinner. It would be an honor to have you.")

#3-6

invitations.append('dad')
invitations.append('brenelle')
invitations.append('marvin gaye')

print(f"\nHello {invitations[3].title()}, I'd like to formally invite you to dinner. It would be an honor to have you.")
print(f"Hello {invitations[4].title()}, I'd like to formally invite you to dinner. It would be an honor to have you.")
print(f"Hello {invitations[5].title()}, I'd like to formally invite you to dinner. It would be an honor to have you.")

print(f"\nGreat news {invitations[0].title()}! I've found a bigger table for more guests.")
print(f"Great news {invitations[1].title()}! I've found a bigger table for more guests.")
print(f"Great news {invitations[2].title()}! I've found a bigger table for more guests.")

#3-7

print("\nHey everyone, unfortunately I can only have two people at dinner now.")
invitations.pop()
invitations.pop()
invitations.pop()
invitations.pop()
print(invitations)

print(f"\nHey {invitations[0].title()}, just wanted to let you know that you're still invited")
print(f"\nHey {invitations[1].title()}, just wanted to let you know that you're still invited")

del invitations[1]

print(invitations)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort #sort function sorts the list in aphabetical order
print(cars)

cars.sort(reverse=True)
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars)) #sored() function allows us to sort the list momentarily

print("\nHere is the original list again:")
print(cars)

cars.reverse() # reverse function is permenant, but you can revert by reversing again
print(cars)
cars.reverse()
print(cars)
len(cars) # the len function tells you how many items are in your list

"""* 3-8 Seeing the World
* 3-9 Dinner Guests
* 3-10 Every Function
"""

#3-8
destinations = ['rio de janerio', "new york", "japan", "paris", "porofino"] #Store locations in a list. Make sure the list is not in alphabetical order
print(destinations) # Print your list in its original order. Don't worry about printing the list neatly, just print it as a row Python list
print("\n")

print(sorted(destinations)) # Use sorted() to print your list in alphabetical order without modifying the actual list
print(destinations) # Show that your list is still in it's original order by printing it
print("\n")

print(sorted(destinations, reverse = True)) # Use sorted() to print your list in reverse alphabetical order without changing the order of the original list
print("\n")

destinations.reverse() # Use reverse() to change the order of your list. Print the list to show that its order has changed
print(destinations)
destinations.reverse() # Use reverse() again to change the oder back
print(destinations)
print("\n")

destinations.sort() # Use sort() to change your list so it's stored in alphabetical order. Print the list to show that it has changed
print(destinations)
print("\n")

destinations.sort(reverse = True) # Use sort to change your lsit so it's stored in reverse alphabetical order
print(destinations)

"""# Avoiding Index Errors When Working with Lists
You will get an index error if you try to return an item from the list that is not there / in that position. If an index error occurs and you can't figure out how to resolve it, try printing your list or just printing the length of your list.
"""

help(sorted) #help function tells python to give you help for things you don't understand

