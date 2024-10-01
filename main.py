# take a list of words separated by commas and replace them with " "

spam = []
while True:
    print("Enter a list of goods to get " + str(len(spam) + 1) + 'or enter nothing to stop')
    name_list = input()
    if name_list == "":
        break
    name_list = spam + [name_list]
print('List to get: ')
for name_list in spam:
    print(" " + name_list)