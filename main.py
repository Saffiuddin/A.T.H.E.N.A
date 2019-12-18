#import threading

def running():
    return

def sleep():
    exit()

TERMINATORS = ("exit","quit","close")

words_file = open("res/words.txt",'r')
words = words_file.read().splitlines()


def checkcmd(cmd):
    if cmd in TERMINATORS:
        sleep()
    for i in cmd.split(' '):
        if i in words:
            pass
        else:
            print("'",i,"' is an unrecognized phrase or command, do enter again")
while(1):
    
    print(">>>Input your command.../")
    cmd = input()
    checkcmd(cmd)
    


words_file.close()