import os
#import csv
import subprocess
import mmap
'''
Objective:
This toolkit can be used to validate and manipulate flat files.

You need to have python 2.7 running in the machine.
To view encrypted files, the private key should be installed in the machine.

Author: Dinesh Jayapathy
Created Date: 04-13-2017
Updated Date: 10-04-2017

'''
def printitems(a):
    try:
        floc=raw_input('Enter the location of the files \n')
        print "The files are"
        b = 1
        for i in os.listdir(floc):
            os.chdir(floc)
            print b,i,str(os.path.getsize(i))+' Bytes'
            b=b+1

    except Exception,e:
        print e

def header(d):
    #open the file and print the top line

    with open('C:\DJ\Python-projects\Data\Behavioral_Risk_Factor_Data__Health-Related_Quality_of_Life__HRQOL_.csv',buffering=100) as f:
        for line in f:
            print line

def enc(a):
    for x in os.listdir(a):
        print x
    #encrypt file

def readencrypted(fpath):
    lines = 5
    s = raw_input('Enter the path of files:\n')
    try:
        for i in os.listdir(s):
            print i
            if os.path.isfile(os.path.join(s, i)):
                os.chdir(s)

                dr = (os.path.join(s, i))  # works
                dr = '/'.join(dr.split('\\'))

                p = subprocess.Popen([r'C:\Program Files (x86)\GNU\GnuPG\pub\gpg.exe', '-d', dr]
                                     , shell=True
                                     , stdout=subprocess.PIPE
                                     , stderr=subprocess.PIPE
                                     )


                e = subprocess.Popen([r'C:\Program Files (x86)\GNU\GnuPG\pub\gpg.exe', '--batch','--list-packets','--verbose', dr]
                                     , shell=True
                                     , stdout=subprocess.PIPE
                                     , stderr=subprocess.PIPE
                                     )

                encMessage=e.stdout.readlines()

                # print 'The linecount is'+str(sum(1 for _ in p.stdout))

                # lc = p.stdout.readline()
                # linecount = len(lc)
                # print linecount


                counter = 1
                file = ''
                while counter <= lines:
                    # print p.stdout.readline()+'\n'
                    l = p.stdout.readline()
                    file = file + l
                    counter += 1



                if file != '':
                    for line in encMessage:
                        print line
                    print file
                else:
                    print p.stderr.readline() + '\ncheck the filename/directory \ncheck the decryption key'

                p.kill()


    except Exception,e:
        print e

def renamef():
    os.chdir(raw_input('Enter the location of the files \n'))
    print os.getcwd()

    try:
        a = raw_input('Enter the string to replace in the filename \n')
        b = raw_input('Enter what to replace it with \n')

        [os.rename(f, f.replace(a, b)) for f in os.listdir('.') if not f.startswith('.')]
        print 'Files have been renamed'

    except Exception, e:
        print e


def rowcount():
    s = raw_input('Enter the location of the files')
    for i in os.listdir(s):
        # print i
        if os.path.isfile(os.path.join(s, i)):
            dr = (os.path.join(s, i))  # works
            dr = '/'.join(dr.split('\\'))
            # print dr
            with open(dr) as f:
                for lineNum, l in enumerate(f):  # i is the count of lines starts from 0 so add 1.
                    pass
            print  'Line count for the file  {}  is {}'.format(i, lineNum + 1)



def readunencrypted():
    p = raw_input("Enter the file path:\n")
    r = raw_input("Enter number of lines to read: \n")
    try:

        for i in os.listdir(p):
            if os.path.isfile(os.path.join(p, i)):
                os.chdir(p)
                count = 0
                print i
                with open(i) as f:  # change your file path here
                    for i in f:
                        if count <= int(r):
                            print count, i
                            count += 1
                            #
                            # if count == 10000:#enter your line number here
                            #     print count, i

    except Exception, e:
        print e




def readline():
    p = raw_input("Enter the file path:\n")
    r = int(raw_input("Enter line number to read: \n"))
    try:

        for i in os.listdir(p):
            if os.path.isfile(os.path.join(p, i)):
                os.chdir(p)
                count = 0
                with open(i) as f:  # change your file path here
                    for i in f:

                        count += 1
                        if count - 1 <= r <= count + 1:
                            print count, i

                            #
                            # if count == 10000:#enter your line number here
                            #     print count, i

    except Exception, e:
        print e





def mainfunction():
    try:

        userinput = raw_input("Enter an option \n a: Preview encrypted files \n b: Preview unencrypted files \n c: Read line from files \n d: Run 'File Parser' \n e: Get file statistics \n f: Rename files \n g: Get Rowcount on files \n h: Exit \n\n Enter Your Choice eg. a \n: ")

        if userinput == 'a':
            print "\nPreview encrypted files"
            readencrypted('a')
            mainfunction()

        if userinput == 'b':
            readunencrypted()
            mainfunction()

        if userinput == 'c':
            readline()
            mainfunction()

        if userinput == 'd':

            p=raw_input('Enter the path \n')
            subprocess.call(['python','csv_parse_dev.py',p])
            mainfunction()

        if userinput == 'e':
            printitems('C:\DJ\Python-projects\DJ')
            mainfunction()

        if userinput == 'f':
            renamef()
            mainfunction()

        if userinput == 'g':
            rowcount()
            mainfunction()

        if userinput == 'h':
            exit()
            mainfunction()
        else:
            print('Invalid input! \n')
            mainfunction()
    except Exception,e:
        print e
        #mainfunction()

print '*'.center(100,'*')
print "Flat File Toolkit".center(100,' ')
print '*'.center(100,'*')
#Function calls go in here
mainfunction()



