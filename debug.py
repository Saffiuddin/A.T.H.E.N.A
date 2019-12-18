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
        for i in cmd.split(' ')
            print("ok")
        else:
            print("Unrecognized command")

#print(words)
if "zebra" in words:
    print("yes")
else:
    print("no")

print(">>>Input your command.../")
cmd = input()
checkcmd(cmd)
print(cmd.split(' '))