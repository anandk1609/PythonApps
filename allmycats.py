catNames = []
while True:
    print("Enter the name of cat " + str(len(catNames) + 1) + " :")
    name = input()
    if name == '':
        break
    catNames = catNames + [name]

print('The cat names are:')
for name in catNames:
    print(name)