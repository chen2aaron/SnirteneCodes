import zipfile
import os
import sys
import time
path = "/home/lworld0x00/Downloads/1.zip"


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


def pojie_zip(path, password):
    if path[-4:] == '.zip':
        zip = zipfile.ZipFile(path, "r", zipfile.zlib.DEFLATED)
        try:
            zip.extractall(
                path="/home/lworld0x00", members=zip.namelist(), pwd=password)
            print ' ----success!,The password is %s' % password
            zip.close()
            return True
        except:
            pass
        print 'error'


def get_pass():
    passFile = open(sys.argv[1], 'r')
    for line in passFile.readlines():
        password = line.strip('\n')
        print 'Try the password %s' % password
        if pojie_zip(path, password):
            break
    passFile.close()


if __name__ == '__main__':
    start = time.clock()
    get_pass()
    print "done (%.2f seconds)" % (time.clock() - start)
