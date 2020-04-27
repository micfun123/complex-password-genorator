import random

print('''
Password Generator
==================
''')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
number = input('number of passwords?')
number = int(number)

length = input('password length?')
length = int(length)

print('here are your passwords:')

print('made by michael parker:')

for pwd in range(number):
  password = ''
  for c in range(length):
    password += random.choice(chars)
  print(password)


  k=input("press close to exit") 