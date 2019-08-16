import os
import subprocess


def cls():
    if os.name in ('nt', 'dos'):
        subprocess.call("cls")
    elif os.name in ('linux', 'osx', 'posix'):
        subprocess.call("clear")
    else:
        print(120 * '\n')


def intro():
    print('{:*^80}'.format('  \x1b[33;1mПроект Эйлера\x1b[0m  '))
    print('{:^80}'.format('\x1b[32mhttp://projecteuler.net/archives\x1b[0m'))
