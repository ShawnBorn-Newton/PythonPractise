

print("Hello Wold")

# Comment

name = "Shawn"
print(name)

name = 15

print("5 + 2 =", 5+2)
print("5 - 2 =", 5-2)
print("5 * 2 =", 5*2)
print("5 % 2 =", 5 % 2)
print("5 ** 2 =", 5**2) # exponant
print("5 // 2 =", 5//2)


print("1 + 2 - 3 * 2=", 1+2-3*2)
print("(1 + 2 -3) * 2 =", (1+2-3)*2)

quote = "\"This has been said"

multi_line_quote = ''' This
Also'''

print("%s %s %s" % ('These are quotes', quote, multi_line_quote))
# Lists
grocery_list = ['Juice', 'Tomatoes', 'Potatoes',
                'Bananas']
print('First Item', grocery_list[0])

grocery_list[0] = "Green Juice"
print('First Item', grocery_list[0])
print(grocery_list[1:3])

other_events = ['Wash Car', 'Pick Up Kids', 'Cash Check']

to_do_list = [other_events, grocery_list]
print(to_do_list)

print((to_do_list[1][1]))

grocery_list.append('Onions')
print(to_do_list)

grocery_list.insert(1, "Pickle")
grocery_list.remove("Pickle")
grocery_list.sort()

del grocery_list[4]
print(grocery_list)

to_do_list2 = other_events + grocery_list
print(len(to_do_list2))
print(max(to_do_list2))
print(min(to_do_list2))
# Tuple
pi_tuple = (3, 1, 4, 1, 5, 9)

new_tuple = list(pi_tuple)
new_list = tuple(new_tuple)

len(new_list)
min(new_list)
max(new_list)
# dictionaries
super_villains = {'Fiddler': 'Isaac Bowin',
                  'Jim Darkmagic': 'Tim Rodgers',
                  'The Pickler': 'Mark Mardon',
                  'Rat Scratch': 'Peter Fin'}

print(super_villains['The Pickler'])

del super_villains['Fiddler']

super_villains['Rat Scratch'] = 'Bob Tim'

print(len(super_villains))

print(super_villains.get('Jim Darkmagic'))

print(super_villains.keys())

print(super_villains.values())

# conditionals

age = 21

if age > 16:
    print('You can drive')
else:
    print('You can not drive yet')

if age >= 21:
    print('Have a drink')
elif age >= 16:
    print('Put the beer down')
else:
    print(' get out')

if (age >= 1) and (age <=18):
    print('You is person')
elif (age == 21) or (age >= 65):
    print('Get a Job')
elif not(age == 30):
    print('Home home Bill your drunk ')
else:
    print('What am I doing')

# looping

for x in range(0, 10):
    print(x, ' ', end="")

print('\n')

for y in grocery_list:
    print(y)

for x in [2, 4, 6, 8, 10]:
    print(x)

num_list = [[1, 2, 3], [10, 20, 30], [100, 200, 300]]

for x in range(0, 3):
    for y in range(0, 3):
        print(num_list[x][y])
