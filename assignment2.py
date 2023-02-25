# Assignment 1
print()
print('Assignment 1')
board = {'Benny', 'Hans', 'Tine', 'Mille', 'Torben', 'Troels', 'Søren'}
management = {'Tine', 'Trunte', 'Rane'}
employees = {'Niels', 'Anna', 'Tine', 'Ole', 'Trunte', 'Bent',
             'Rane', 'Allan', 'Stine', 'Claus', 'James', 'Lars'}


not_employee = board.difference(employees)
print(not_employee)  # alle dem der er i det ny set er ikke employees


also_employee = board.intersection(employees)
print(also_employee)  # printer kun navne der er i begge set

management_also_board_member = management.intersection(board)
print(len(management_also_board_member))  # gør som linje 12


management_also_employee = employees.intersection(management)
# intersection() = tager fælles elementer i 2 sets
print(management_also_employee)

management_also_board_members = management.intersection(board)
print(management_also_board_members)

common_in_all_sets = board.intersection(management, employees)
print(common_in_all_sets)

employee_notinboard_or_management = employees.difference(board, management)
print(employee_notinboard_or_management)
print('---------------------------------------------')
print()


# Assignment 2
print("Assignment 2")

my_dict = {'a': 'Alpha', 'b': 'Beta', 'g': 'Gamma'}

# items() = bruges til at returnere en liste af key/value par fra et dictionary
list_of_tuples = [(k, v) for k, v in my_dict.items()]
print(list_of_tuples)
print('---------------------------------------------')
print()

# Assignment 3
print('Assignment 3')

# union = creates a new set that contains all the element from both sets
set1 = {'a', 'e', 'i', 'o', 'u', 'y'}
set2 = {'a', 'e', 'i', 'o', 'u', 'y', 'æ', 'ø', 'å'}
union_set = set1.union(set2)
print(union_set)


# symmetric difference = finder unikke i hver set
symmetric_diff = set1.symmetric_difference(set2)
print(symmetric_diff)


# kommer an på hvilket set man skriver først
difference = set1.difference(set2)
print(difference)

disjoint = set1.intersection(set2)
print(disjoint)
print('---------------------------------------------')
print()

# Assignment 4
print('Assignment 4')


def date_decoder(date):  # takes a date argument
    months = {  # creating a dictionary called month. Maps the abbreviated name to its corresponding number
        'JAN': 1,
        'FEB': 2,
        'MAR': 3,
        'APR': 4,
        'MAY': 5,
        'JUN': 6,
        'JUL': 7,
        'AUG': 8,
        'SEP': 9,
        'OCT': 10,
        'NOV': 11,
        'DEC': 12
    }

    # splits the date to 3 items using '-' seperator/character and assigns each to day, month, year variables
    day, month, year = date.split('-')
    # looks up in dictionary and assigns corresponding value of the abbreviated key
    month = months[month]
    year = '20' + year if int(year) <= 23 else '19' + year
    # creates a tuple by inclusing commas between values
    return int(year), month, int(day)


print(date_decoder('08-APR-14'))
print('---------------------------------------------')
print()
