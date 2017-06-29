# myPets from Chapter 4

petNames = ['Meaty', 'Scully', 'Mr. Meyhem', 'Reaper', 'Pandora', 'Lucy', 'Bacon']
print('Enter a pet name:')
name = input()
if name not in myPets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')
