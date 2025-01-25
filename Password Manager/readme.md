# Password Manager 

It's a simple passowrd managing python script which will allow:
    1. adding a password
    2. see the password 

Encryption of text file is possible due to **cryptography** module called as **Fernet**
```python
from cryptography.fernet import Fernet
# this module is allowing us to encrypt and decrypt our password
```

*What does it do:*
key + password + text to encrypt = random text
random text + key + password = text to encrypt

**Basically to encrypt and decrypt** you need both key and master password.

## Note:
when you write 
```python
b'hello'
```
it is in byte string, compare to this which is in normal string
```python
'hello'
```
- *.decode()* to change from byte string to normal string
- *.encode()* to change from normal string to byte string
  
How password_manager.py script works:


