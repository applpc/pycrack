#Note: THIS WILL TAKE A LONG TIME TO CRACK A HASH!!! The upside of using this is that it tests indefinitely until it finds your hash.

import itertools
import hashlib
from hashlib import md5
import time
import sys

#List of Characters Used In Combinations
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '@', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

num = 0

srchash= raw_input("Hash to be Cracked:")

#Every Possible Combination of Characters Generator
def main():
    global num
    for abc in itertools.product(alphabet, repeat = num):
        randomabc=''.join(abc)

        def computeMD5hash(randomabc):
            m = hashlib.md5()
            m.update(randomabc.encode('utf-8'))
            return m.hexdigest()
        abchash= computeMD5hash(randomabc)

    #If Provided Hash = Generated Hash Print Plain Text
        if abchash==srchash:
            on = False
            print "There is your password:"
            abc = str(abc).replace("'", "")
            abc = abc.replace(",", "")
            abc = abc.replace(")", "")
            abc = abc.replace("(", "")
            abc = abc.replace(" ", "")
            print abc
            raw_input("Press enter to close")
while True:
    num= num + 1
    main()
    print("Done testing "+ str(num) + " length hashes")
