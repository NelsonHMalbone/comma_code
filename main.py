# take a list of words separated by commas and replace them with " "

spam_list = []
while True:
    print("Enter a list of goods to get " + str(len(spam_list) + 1) + ' or enter nothing to stop')
    name_list = input()
    if name_list == "":
        break
    spam_list = spam_list + [name_list]
print('List to get: ')
for name_list in spam_list:
    print(" " + name_list)