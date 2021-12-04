#A great utility to generate strong passwords--
import sys
import string
import random

CHAR = string.ascii_letters+string.ascii_uppercase+string.ascii_letters+string.punctuation
CHAR = list(CHAR)
LENGTH = 30

#print(CHAR)
def pass_cmd():
    passw=""
    passwd=''
    passwd_chr = sys.argv[1]
    for c in CHAR:
        for d in passwd_chr:
            passw += c
            passw += d
    iterations=1
    while iterations<= LENGTH:
        passwd += random.choice(passw)
        iterations +=1
    print(passwd)
    inp = input("would you like to save it? [Y/N] ")
    inp=inp.lower()
    if inp == 'y':
        name=input('name of file? > ')
        with open(name, 'w') as f:
            f.write(passwd)
    elif inp=='n':
        print("thanks for using!")
        exit(0)
    else:
        exit(0)

        

        

pass_cmd()


def pass_int():
    pass



def main():
    if sys.argc <= 1:
        pass_int()
    else:
        pass_cmd()




        

