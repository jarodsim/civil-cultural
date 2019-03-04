import SSocket
import threading
import json
import time
import urllib.parse

rv = True

SSocket.Server_wait(1000, 23125)


def main_loop():
    while rv:
        SSocket.Server_accept()
        SSocket.Write("HTTP/1.1 200 OK\n"
                      + "Content-Type: text/html\n"
                      + "\n"
                      + "<html><body><center><h1>Recived!</h1></center></body></html>\n");
        request = SSocket.Read(10000)
        print(request)
        a = request.split(" ")
        print(a)
        b = a[1]
        b = b.replace("%20", "-")
        print(b)
        c = b[1:]
        print(c)
        d = urllib.parse.unquote(c)
        print(d)
        SSocket.Connect("127.0.0.1", 2312)
        SSocket.Write(str(d))

while rv:
    main_loop()