from collections import Counter

boardOfDirectors = {'Benny', 'Hans', 'Tine', 'Mille', 'Torben', 'Troels', 'Søren'}
management = {'Tine', 'Trunte', 'Rane'}
employees = {'Niels', 'Anna', 'Tine', 'Ole', 'Trunte', 'Bent', 'Rane', 'Allan', 'Stine', 'Claus', 'James', 'Lars'}

# who in the board of directors is not an employee?
def directorNotEmployee():
    li = []
    for x in boardOfDirectors:
        if x not in employees:
            li.append(x)
    print(f'these directors are not emplyees: {li}')

# who in the board of directors is also an employee?
def directorAndEmployee():
    for x in boardOfDirectors:
        if x in employees:
            print(f'this director is also an emplyee: {x}')

# how many of the management is also member of the board?
def managerAndBoard():
    count = 0
    for x in management:
        if x in boardOfDirectors:
            count = count +1
    print(f'there is: {count} manager who is also a member of the board')

# All members of the managent also an employee
def allManagersAlsoEmployee():
    isManAlsoEmp = True
    for x in management:
        if x not in employees:
            isManAlsoEmp = False
    print(isManAlsoEmp)

# All members of the management also in the board?
def allManagersAlsoBoard():
    isManAlsoBoa = True
    for x in management:
        if x not in boardOfDirectors:
            isManAlsoBoa = False
    print(isManAlsoBoa)

# Who is an employee, member of the management, and a member of the board?
def whoIsAll():
    for x in management:
        if x in boardOfDirectors:
            if x in employees:
                print(f'{x} is both an employee, a manager and a member of the board')

# Who of the employee is neither a memeber or the board or management?
def employeeIsNotBoardOrManagement():
    li = []
    for x in employees:
        if x not in boardOfDirectors:
            if x not in management:
                li.append(x)
    print(f'{li} is not on the board or managers')

# Using a list comprehension create a list of tuples from the folowing datastructure
def listComprehension():
    datastructure =  {'a': 'Alpha', 'b' : 'Beta', 'g': 'Gamma'}
    li = [(k,v) for k,v in datastructure.items()]
    print(li)
    
# From these 2 sets:
def twoSets():
    #Union
    li = {'a', 'e', 'i', 'o', 'u', 'y'}
    li2 = {'a', 'e', 'i', 'o', 'u', 'y', 'æ' ,'ø', 'å'}
    union = li.union(li2)
    print(union)
    # Symmetric difference
    symmetricDifference = li.symmetric_difference(li2)
    print(symmetricDifference)
    # Difference
    difference = li2.difference(li)
    print(difference)
    # Disjoint
    disjoint = li.isdisjoint(li2)
    print(disjoint)

# Date decoder
def dateDecoder(x):
    monthDecoder = {
        "JAN" : 1,
        "FEB" : 2,
        "MAR" : 3,
        "APR" : 4,
        "MAJ" : 5,
        "JUN" : 6, 
        "JUL" : 7,
        "AUG" : 8,
        "SEP" : 9,
        "OKT" : 10,
        "NOV" : 11,
        "DEC" : 12
        }
    z = x.split('-')
    newDate = ('19' + z[-1], monthDecoder[z[1]], z[0])
    print(newDate)

dateDecoder("10-DEC-95")
