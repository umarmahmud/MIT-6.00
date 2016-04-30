# Paste your code into this box
ceiling = 100
base = 0
number = (ceiling + base) / 2
answer = ''

print 'Please think of a number between 0 and 100!'
print 'Is your secret number ' + str(number) + '?'

while (True):

    answer = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

    if answer == 'l':
        base = number
        
    elif answer == 'h':
        ceiling = number
        
    elif answer == 'c':
        break
    
    elif answer != 'l' or answer != 'h' or answer != 'c':
        print ('Please enter valid choice')

    number = (ceiling + base) / 2
        
    print 'Is your secret number ' + str(number) + '?'
        
print 'Game over. Your secret number was: ' + str(number)

