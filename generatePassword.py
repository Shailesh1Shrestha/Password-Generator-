import random

length = int(input("Enter the length of password \n"))
c = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
pass = "".join(random.sample(c,length))
print(pass)
