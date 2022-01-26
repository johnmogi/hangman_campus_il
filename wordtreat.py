import os

wordlist = []

with open('wordlist', 'r') as fix:
    lines = fix.readlines()
    for line in lines:
        line = line.split(' \n')
        wordlist.append(line)

if __name__ == '__main__':
    print(wordlist)