from cryptography.fernet import Fernet

''' after running this below function once, commenting it
def write_key():
    key = Fernet.generate_key()
    # wb is writebytes mode
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

# implementing master password was little complex/hard, so he skipped it in the tutorial.
# master_pwd = input("What's the master password?")
key = load_key() # + master_pwd.encode()
fer = Fernet(key)

# this is simplified below, its not really +
# key + master_pwd + text to encrypt = random text
# random text + key + master_pwd = text to encrypt

def view():
    # by me - if no data then print nothing here yet.
    with open("passwords.txt", "r") as f:
        print()
        for line in f.readlines():
            # to remove the \n in everyline in txt file
            data = line.rstrip()
            user, passw = data.split('|')
            print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())
        print()


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    # w mode will override the file if it already exists already
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input("Would you like to add a new password or view existing ones (view, add)? To quit press (q) ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue

