dict.py v1.0
import sys
import itertools


def lworld0x00():
    print "***************************"
    print "*******Code For Fun********"
    print "    /\____________/\       "
    print "    \              /       "
    print "     \    hello   /        "
    print "      \   world  /         "
    print "       \________/          "
    print "                           "
    print "*******by 1world0x00*******"
    print "***************************"


def setLowerWord():
    words = "abcdefghijklmnopqrstuvwxyz"
    num = int(sys.argv[2])
    fp = open(sys.argv[1], "wb+")
    # fp=open("2.txt","wb+");
    # num=2
    if(sys.argv[2] == 0):
        fp.close()
    else:
        i = 0
        while(i <= 25):
            tmp = words[0:num]
            i += 1
            for j in itertools.permutations(tmp, num):
                fp.writelines("".join(j))
                fp.writelines("\n")
            words = words[1:]
        fp.close()


def setUpperWord():
    words = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num = int(sys.argv[3])
    fp = open(sys.argv[1], "a+")
    # fp=open("2.txt","a+")
    # num=2
    if(sys.argv[3] == 0):
        fp.close()
    else:
        i = 0
        while(i <= 25):
            tmp = words[0:num]
            i += 1
            for j in itertools.permutations(tmp, num):
                fp.writelines("".join(j))
                fp.writelines("\n")
            words = words[1:]
        fp.close()


def setNum():
    words = "1234567890"
    num = int(sys.argv[4])
    fp = open(sys.argv[1], "a+")
    # fp=open("2.txt","a+")
    # num=2
    if(sys.argv[4] == 0):
        fp.close()
    else:
        i = 0
        while(i <= 10):
            tmp = words[0:num]
            i += 1
            for j in itertools.permutations(tmp, num):
                fp.writelines("".join(j))
                fp.writelines("\n")
            words = words[1:]
        fp.close()

# def dict():
    # print "name:",sys.argv[0]
    # print "first:",sys.argv[1]
    # print "second:",sys.argv[2]

if __name__ == "__main__":
    lworld0x00()
    # dict();
    # fp=open("2.txt","wb+")
    setLowerWord()
    setUpperWord()
    setNum()
