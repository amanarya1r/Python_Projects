import os #this module have a functionality to interact with the operating system so that any can interact with files, directorie, handle environment variables and more.
from cryptography.fernet import Fernet
# this module is allowing us to encrypt and decrypt our password

#It is still in the starting phase so I can not rely on it

def write_key():
    if not os.path.exists("key.key"):
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file: # wb means write in bytes
            # this function create key.key file 
            key_file.write(key)

write_key()

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()  # we can also all this thing by just using with automatically
    return key

# mpwd = input("What is the master password?\n: ")  #? You don't need to you use mpwd because I don't know how to use it properly
mpwd = "12345"

key = load_key() + mpwd.encode()  # since key in bytes than mpwd also have to be in bytes

fer = Fernet(key) # its intializing this module

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()  # rstrip and strip will cut the new line
            user, passw = data.split("|") # .split will take a line and look for '|' and it will split the line
            # "hello|tim|yes|2" ==> ["hello", "tim", "yes", "2"]
            print("\nUser: ", user, "\nPassword: ", fer.decrypt(passw.encode()).decode()) 

def add():
    name = input('\nAccount Name: ')
    psrd = input("Password: ")

    with open('passwords.txt', 'a') as f:  #a for append w for overwrite and r for read mode. a do the things of both w and r
        #with always us to do things into the file
        f.write(name + "|" + fer.encrypt(psrd.encode()).decode() + "\n")
        

    # file = open('passwords.txt', 'a')
    # file.close() 
    # #we have to close the file manually after working on it 
    # #this is all be done using with
    


while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit?\n: ").lower()
    if mode == "q":
        break
    
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else: 
        print("Invalid mode.")
        continue