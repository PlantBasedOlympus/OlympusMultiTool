
import time
from time import sleep



def mainmenu():
    print('╔═══════════════════════════════════════════════════════╗')
    print('             v1.0      Main Menu    Welcome ')
    print('╟═══════════════════════════════════════════════════════╣')
    print('║    1 > Amazon Store Card   |    6 > IP Pinger         ║')
    print('║    2 > Amazon Store Card   |    7 > IP Pinger         ║')
    print('║    3 > Amazon Store Card   |    8 > IP Pinger         ║')
    print('║    4 > Amazon Store Card   |    9 > IP Pinger         ║')
    print('║    5 > Amazon Store Card   |    10 > IP Pinger        ║')
    print('╠═══════════════════════════════════════════════════════╣')
    print('║ C > Credits   |   N > Next Page      |  S > Settings  ║')
    print('╚═══════════════════════════════════════════════════════╝')
    print('        Write a number OR "HELP" and press {Enter}       ')
    maininput = input('[olmp@input] > ')

    if maininput == 'n' or maininput == 'N':
        mainmenu2()
    elif maininput == 'Credits' or maininput == 'credits' or maininput == 'credit' or maininput == 'Credit' or maininput == 'c' or maininput == 'C':
         print('Owner - Chriss\nCo - Owner N/A\nDevelopers - Chriss\nUI Design - Chriss')
    elif maininput == 'HELP' or maininput == 'help':
         print('are you retarted?')


def adminmenu():
    print('hi')




def mainmenu2():
        print('╔═══════════════════════════════════════════════════════╗')
        print('          v1.0      Main Menu    Welcome ' + username1)
        print('╟═══════════════════════════════════════════════════════╣')
        print('║   11 > Amazon Store Card   |    16 > IP Pinger        ║')
        print('║   12 > Amazon Store Card   |    17 > IP Pinger        ║')
        print('║   13 > Amazon Store Card   |    18 > IP Pinger        ║')
        print('║   14 > Amazon Store Card   |    19 > IP Pinger        ║')
        print('║   15 > Amazon Store Card   |    20 > IP Pinger        ║')
        print('╠═══════════════════════════════════════════════════════╣')
        print('║    C > Credits  |   B > Back Page   |  S > Settings   ║')
        print('╚═══════════════════════════════════════════════════════╝')
        print('        Write a number OR "HELP" and press {Enter}       ')
        maininput1 = input('[olmp@input] > ')


        if maininput1 == 'B' or maininput1 == 'b':
             mainmenu()


mainmenu()
