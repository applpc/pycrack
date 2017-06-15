#Written by Kenny Adams
#Updated for Python 2.7.13

import hashlib
import time

print("1.) MD5")
print("2.) SHA-1")

hashtype= raw_input("Pick a hashing type:")
srcpwd= raw_input("Type in The Password You Would like to be Hashed:")

def computeMD5hash(srcpwd):
        m = hashlib.md5()
        m.update(srcpwd.encode('utf-8'))
        return m.hexdigest()
def computeSHA1hash(srcpwd):
        m = hashlib.sha1()
        m.update(srcpwd.encode('utf-8'))
        return m.hexdigest()
print
print ("Here is Your Hashed Password:")
if hashtype == "1":
        print (computeMD5hash(srcpwd))
if hashtype == "2":
        print (computeSHA1hash(srcpwd))

time.sleep(10)


