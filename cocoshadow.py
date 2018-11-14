#!/usr/bin/python
# Coconut Motherfucker Shadow Cracker
# Version: 1.1
# coded by: Carlos Néri Correia
# additional code and comments by: Danilo Santos
# Implemented and tested using python 3.6.7rc1 on a Linux environment

import crypt
import sys, argparse
import os.path

print('''
+------------------------------------------------------+
|   + + +  Coconut Motherfucker Shadow Cracker + + +   |
|             coded by: Carlos Néri correia            |
|    additional code and comments by: Danilo Santos    |
|                  github.com/hackerama                |
|                  github.com/dsantos-1                |
+------------------------------------------------------+
''')

# Checks if a line is syntactically correct
def find(line):
    for l in line:
        if l==('$'):
            return True
    return False

# Gets the hashed password and its salt value from a valid line
def parse(line):
    global parse1, parse2, salt
    parse1=line.split(':')
    parse2=parse1[1].split('$')
    salt='$' + parse2[1] + '$' + parse2[2] + '$'
    return 0

# Uses the wordlists passed as a parameter to attempt to crack the hashed password
def brute(args):
    for f in args.wlist.split(','):
        if(os.path.exists(f)):
            with open(f, 'r') as brute: 
                print('--- Current wordlist: %s ---' % f)

                for senha in brute:
                    senha=senha.rstrip()
                    r=crypt.crypt(senha, salt)
                    if(args.verbosity):
                        print('Attempting %s as password... ' % (senha), end=''),
                    if r==parse1[1]:
                        if(args.verbosity):
                            print('success.\n')
                        print('User: '+parse1[0]+'\nPassword: '+senha)

                        return
                    else:
                        if(args.verbosity):
                            print('failure.')
                print('')
        else:
            sys.exit('Error: the file %s was not found' % f)

def main():
    # Structure that organizes the command line parameters
    parser=argparse.ArgumentParser(description='This tool attempts to crack a hashed Unix password, given a shadow file and a list of password files in plain text.')
    parser.add_argument('shadow_file', help='shadow file\'s name')
    parser.add_argument('wlist', help='wordlist or list of wordlists in plain text. The filenames must be separated by commas and must not contain spaces. Example:\nwordlist1,wordlist2,...,wordlistn')
    parser.add_argument('-v', '--verbosity', help='increase output verbosity', action='store_true')

    args=parser.parse_args()
	
    # Checks if the shadow file exists
    if(os.path.exists(args.shadow_file)):
        with open(args.shadow_file, 'r') as string:
            for line in string:
                if(find(line) is True):
                    parse(line)
                    brute(args)
    else:
        sys.exit('Error: the shadow file was not found')

if __name__=='__main__':
    main()
