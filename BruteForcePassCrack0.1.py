# Written by Kenny Adams
#Updated for Python 2.7.13 on 2/15/17
#Original Name "Decryptor Ext. List v.Alpha 0.4.py"

import hashlib
import itertools

input_hash = raw_input("What's the Hash that you want to be Cracked?:")
min_limit = raw_input("What is the Minimum Password Length?:")
max_limit = raw_input("What is the Maximum Password Length?:")
min_limit = int(float(min_limit))
max_limit = int(float(max_limit))
numrange = range(min_limit, max_limit)
dict = "dict.txt"
item= 0
numtogen= numrange[item]
listcount = int(len(numrange) + 1)


list= {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '@', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '[', '}', ']', '|'}

file = open("dict.txt", "w")

#NumGen Seq
def randomgen():
    #Declare Variables as Global
    def numgenmainseq():
        global numtogen
        for i in range(listcount):
            for abc in itertools.product(list, repeat= numtogen):
                randomabc = ''.join(abc)
                file.write(randomabc + "\n")
                numtogen = numrange[item + 1]
            print("Done ")
    numgenmainseq()
    for abc in itertools.product(list, repeat=max_limit):
        randomabc = ''.join(abc)
        file.write(randomabc + "\n")

randomgen()
print("Done Generating Range Combos.")


def main():
    with open(dict) as fileobj:
        for line in fileobj:
            line = line.strip()
            line.encode('utf-8')
            if hashlib.md5(line).hexdigest() == input_hash:
                print (line)
                return ""
    print ("Failed to crack the hash.")


if __name__ == "__main__":
    print("Your Password is:")
    print(main())




