# Note: Make sure that your dictionary file that you have saved to your computer is either in the same directory as this program 
# and named "dict.txt", or you change the "dict" variable to the directory of your file.

import hashlib
import time

input_hash = raw_input("What's the Hash that you want to be Cracked?:")
dict = "dict.txt"

def main():
    with open(dict) as fileobj:
        for line in fileobj:
            line = line.strip()
            if hashlib.md5(line).hexdigest() == input_hash:
                print (line)
                return ""
    print "Failed to crack the hash."

if __name__ == "__main__":
    print ("Your Password is:")
    print main()
