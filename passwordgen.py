import random
import pyperclip
import sys

text = '1234567890QWERTYUIOP[]\ASDFGHJKLZXCVBNM./qwertyuiopasdfghjklzxcvbnm;:<>?{}#%!()_-=+'
alphabet = list(text)

print('Select your password length (Limit is 100)')
k = None
while k not in range(0, 101):
        try:
            k = int(input('> '))
            if k in range(0, 101):
                list = random.sample(alphabet, k=k)
                password = ''.join(list)
                print("Here's your password:", password)
                break
            else:
                print('Try again.')
        except ValueError:
            print('Please enter a valid number.')

retry = input('Do you want to retry? y/n ')

if retry == 'y':
    print("Here's your password:", password)

    copy = input('Do you want to copy it? y/n ')
    if copy == 'y':
        pyperclip.copy(password)
        print('Copied.')
        input('Press enter to quit.')
        sys.exit(1)
    else:
        input('Press enter to quit.')
        sys.exit(1)
else:
    copy = input('Do you want to copy it? y/n ')
    if copy == 'y':
        pyperclip.copy(password)
        print('Copied.')
        input('Press enter to quit.')
        sys.exit(1)
    else:
        input('Press enter to quit.')
        sys.exit(1)