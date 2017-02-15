import hashlib
import time

srcpwd= raw_input("Type in The Password You Would like to be Hashed:")

def computeMD5hash(srcpwd):
        m = hashlib.md5()
        m.update(srcpwd.encode('utf-8'))
        return m.hexdigest()
print
print ("Here is Your Hashed Password:")
print (computeMD5hash(srcpwd))

time.sleep(10)


