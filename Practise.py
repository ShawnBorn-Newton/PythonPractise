

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




