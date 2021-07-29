name = input('What is your name? ')
password = input('Please enter your password: ')
if name == 'Ray':
    print('Hello, Ray!')
    if password == 'swordfish':
        print('Access Granted')
    else:
        print('Access Denied')
else:
    print('Access Denied')
