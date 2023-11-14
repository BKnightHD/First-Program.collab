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

car_companies = ['hodna', 'bmw', 'mercedes-benz', 'toyota', 'ford']
print(car_companies)
car_companies.append('kia') #append method add kia to the end of the list
print(car_companies)

motercycles2 = []
motercycles2.append('honda')
motercycles2.append('yamaha')
motercycles2.append('suzuki')
print(motercycles2[0].title())
print(motercycles2)
motercycles2.insert(0, 'ducati') #insert will pick a specific spot to intert the new value into the list
print(motercycles2)
#Sometimes you'll want to remove an item or a set of items from a list. Use the del function in this case
del motercycles2[0]
print(motercycles2)
popped_motercycles = motercycles2.pop()
print(motercycles2)
print(popped_motercycles) #popped will show up the value of the item that was removed or "popped" from the lsit