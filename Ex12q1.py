# What is wrong with this?
cheese = ['Cheddar', 'Stilton', 'Cornish yarg']
print(cheese)
# cheese += 'Oke'
# print(cheese)

# This will add the individual characters from the string 'Oke' as items to the list 'cheese'.
# Instead, we should add 'Oke' as an item to the end of the list in this way:

# cheese += ['Oke']
# Or:
cheese.append('Oke')
print(cheese)

# We can add two new cheeses to the list with the single command:

cheese += ['Brie', 'Edam']
print(cheese)

