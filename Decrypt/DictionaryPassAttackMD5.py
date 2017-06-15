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
