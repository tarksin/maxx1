a=[1,2,"alpha"]
b=[2,3,'alpha']

# print (a[2] is b[2])
def return_animals():

    animals = [
        {'dog': "Willie"},
        {'cat': "Xumi"},
        {'parrot': "Lucifer"},
        {'goat': "Morris"},
        {'hen': "Ralfie"}
        ]

    return animals;

x = return_animals()
# print(x)
for (idx,  item) in enumerate(x):
    print(idx, item.keys(),   ':', item.values())

director = 'Margaret Zavala, PhD'
if 'Ph D' in director:
    print('QUALIFIED')
else:
    print("No advanced degree")

