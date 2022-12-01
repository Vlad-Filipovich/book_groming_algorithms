# products = ['apple', 'milk', 'avocado']
# prices = [0.67, 1.49, 1.49]
#
# book = dict(zip(products, prices))
#
# print(book)
#
# print(book['avocado'])

voted = {}


def check_voter(name):
    if voted.get(name.lower()):
        print('Oh! According to our records, you have already voted.')
    else:
        print('You can vote!')
        choice = input('Please make your choice: ')
        while choice.lower() not in ['no', 'yes']:
            print('You can only choose "Yes" or "No"')
            choice = input('Please make your choice: ')
        voted[name.lower()] = choice.lower()


while True:
    check_voter(input('Please enter your name: '))
    if input('Shall we continue?\n').lower() == 'no':
        break


print(voted)
