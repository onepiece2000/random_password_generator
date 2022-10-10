import random
characters = "01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ&*()[]|/\?!@#$%^abcdefghijklmnopqrstuvwxyz"
password_length = int(input('Enter the length of the password: '))
password = "".join(random.sample(characters, password_length))
print("Gernerated password: %s" %password)
