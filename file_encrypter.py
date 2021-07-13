import json
import random
#.json file that stores users passwords and keys
dbfilename = '/Users/andreasneacsu/Projects/Python/passwordencrypt/passwords.json'
#function that will scramble the alphabet and numbers 0-9 to create a unique encryption 
def shuffle(word):
    word = list(word)
    random.shuffle(word)
    key = ''.join(word)
    return key
#stores our original charachters 
decrypted1 = 'abcdefghijklmnopqrstuvwxyz1234567890 '
#stores our unique ecryption
encrypted1 = shuffle(decrypted1)
#turns the string into a bytes data type
bytes_enc = str.encode(encrypted1)
bytes_dec = str.encode(decrypted1)
#translates from dec -> enc
scrambled = bytes.maketrans(bytes_dec, bytes_enc)
#translates from enc -> dec
unscrambled = bytes.maketrans(bytes_enc, bytes_dec) 

#funtion to take any text and use the above data to encrypt
def encrypt(text):
     encryptedpass = text.translate(scrambled)
     return(encryptedpass)
#funstion to store user data to .json
def dumpinf():
    print("Create new password for your file")
    p = input("> ")
    userinfo = {p: encrypted1}
    with open(dbfilename, "r+") as file:
        data = json.load(file)
        data.update(userinfo)
        file.seek(0)
        json.dump(data, file)
#main encrypting funtction handles writing new encrypted version to the file    
def encrypting():
    dumpinf()
    filecontent = open(usrfile , 'r+')
    contentvar = filecontent.read()
    uf = open(usrfile , "w")
    uf.truncate(0)
    uf.write(encrypt(contentvar))
    print('> done, file hase been encrypted.')
#main decrypting function handles grabbing info from .json, decrypting and writing to the file
def decrypting():
    print('> enter your passcode')
    upass = (input("> "))
    with open(dbfilename, "r+") as file:
        dict = json.load(file)
    key = dict[upass]
    bytes_key = str.encode(key)
    txt = bytes.maketrans(bytes_key, bytes_dec)
    filecontent = open(usrfile , 'r+')
    contentvar = filecontent.read()
    uf = open(usrfile , "r+")
    uf.truncate(0)
    uf.write(contentvar.translate(txt))
    print('> done, file has been decrypted')

#main ui
print('> Enter filename and path here')
usrfile = input("> ")

print('''
    > enter a 1 to encrypt
    > enter a 2 to decrypt
    > enter a 0 to quit
            ''')
usrchoice = input('> ')

if usrchoice == '1':
    encrypting()
elif usrchoice == '2':
    decrypting()
elif usrchoice == '0':
    print(' ') 
else:
    print('> improper answer')
