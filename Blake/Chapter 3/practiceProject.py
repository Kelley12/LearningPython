# Practice Project from Chapter 3: the Collatz Sequence

def collatz(number):
    if number % 2 == 0:
        number = number//2
        print(str(number))
        return number
    else:
        number = 3 * number + 1
        print(number)
        return number

def main():
    print('Enter a number:')
    try:
        usersNumber = int(input())
        
        while usersNumber != 1:
            usersNumber = collatz(usersNumber)
    except:
        print('Error: You must enter number you idiot!')
        main()

print('*** Collatz Sequence ***')
print('Enter a number ans using the collatz sequence it will eventually end up at 1')
print('')   
main()
