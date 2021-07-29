# elif statements are executed in order. This example shows two different outputs if the elif statements are incorrectly ordered.

name = input('What is your name? ')
age = int(input('What is your age? '))

# This section shows the correct elif order
print('=== Correct Example ===')
if name == 'Ray':
    print('Hi, Ray!')
elif age < 32:
    print('You are not Ray, kiddo.')
elif age > 2000:
    print('Unlike you, Ray is not an undead, immortal vampire.')
elif age > 32:
    print('You are not Ray, oldie.')

# This section shows an incorrect elif order
print('=== Incorrect Example ===')
if name == 'Ray':
    print('Hi, Ray!')
elif age < 32:
    print('You are not Ray, kiddo.')
elif age > 32:
    print('You are not Ray, oldie.')
elif age > 2000:
    print('Unlike you, Ray is not an undead, immortal vampire.')
