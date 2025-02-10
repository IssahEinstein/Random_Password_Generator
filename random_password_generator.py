# collect user preferences
# - length
# - should contain uppercase
# - should contain special charx's
# - should contain digits

# get all available characters
# randomly pick characters up to length
# at least one of each specified character type
# make sure length matches criteria of user

import random
import string

def generate_password():
    """"""
    length = int(input("Enter the desired length for your password:\n").strip())
    include_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower()
    include_special = input("Include special characters? (yes/no): ").strip().lower()
    include_digits = input("Include digits? (yes/no): ").strip().lower()

    if length < 4:
        print("Password length must be at least four characters")
        return
    
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if include_special == 'yes' else ""
    special = string.punctuation if include_special == 'yes' else ""
    digits = string.digits if include_digits == 'yes' else ""

    all_characters = lower + upper + special + digits

    required_characters = []

    if include_uppercase == 'yes':
        required_characters.append(random.choice(upper))
    if include_special == 'yes':
        required_characters.append(random.choice(special))
    if include_digits == 'yes':
        required_characters.append(random.choice(digits))
    
    remaining_length = length - len(required_characters)
    password = required_characters

    for _ in range(remaining_length):
        character = random.choice(all_characters)
        password.append(character)
    
    random.shuffle(password)

    str_password = "".join(password)

    return str_password

password = generate_password()
print("\nYour password is:")
print(password)