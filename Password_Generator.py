import random
import string

def generate_random_password(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

length = int(input("Enter the desired password length: "))
print(f"Generated password: {generate_random_password(length)}")
