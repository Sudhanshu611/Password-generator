import random
import string

len_pass = int(input("How long your password must be? => "))
num_pass = int(input("How many passwords you want? => "))
password = ""
def generator():
    global password
    char = string.punctuation + string.ascii_uppercase + string.ascii_lowercase + string.digits
    for i in range(len_pass):
      password += random.choice(char)

for x in range(num_pass):
    generator()
    print(password)
    password = ""