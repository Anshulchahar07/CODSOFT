import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%^*()"
length = int(input("Enter Length :"))
password = ""

for a in range(length):
    password += random.choice(chars)
print(password)3