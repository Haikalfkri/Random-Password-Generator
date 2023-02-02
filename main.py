import random
import string

pwd_combination = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def password_generator():
    pwd_length = int(input("How long random password do you want? "))

    random_password = []
    for pwd in range(pwd_length):
        random_password.append(random.choice(pwd_combination))

    password = "".join(random_password)
    print(f"Your password is: {password}")


if __name__ == "__main__":
    password_generator()