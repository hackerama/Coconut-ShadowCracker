#!/usr/bin/python
#-*-coding:utf:8-*-
#Coconut Motherfucker Shadow Cracker
#Version: 1.0
#coded by: Carlos Néri Correia

import crypt
import sys

print '''
        +------------------------------------------------------+
        |   + + +  Coconut Motherfucker Shadow Cracker + + +   |
        |             coded by: Carlos Néri correia            | 
        |                  github.com/hackerama                |
        +------------------------------------------------------+
'''
def find(line):
    for l in line:
        if l == ("$"):
            return True
    return False


def parse(line):
    global parse1, parse2, salt
    parse1 = line.split(':')
    #print parse1[1]
    parse2 = parse1[1].split('$')
    salt = "$" + parse2[1] + "$" + parse2[2] + "$"
    return 0; 


def brute():
    with open ('wlist.txt', 'rb') as brute: 
        for senha in brute:
            senha = senha.rstrip()
            r = crypt.crypt(senha, salt)
            if r == parse1[1]:
                print '''
            [+] Senha encontrada:
                Usuario: '''+parse1[0]+'''
                Senha: '''+senha

def main():
    if len(sys.argv) < 2 or sys.argv[1] == "-h":
        print'''
                    USAGE cocoshadow.py [SHADOWFILE]
            '''
        sys.exit(0)
    with open (sys.argv[1], 'rb') as string:
        for line in string: 
            if find(line) is True:
                parse(line)
                brute()

if __name__ == "__main__":
    main()
