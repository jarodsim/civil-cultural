import SSocket
import hashlib

username = "wi6n3l"
print("username is: ", username)

password = hashlib.sha224(str(23125899).encode("utf-8")).hexdigest()

print("password hash is: ", password)

rv = True

SSocket.Connect("127.0.0.1", 2312)


SSocket.Write(r"DB-REQUEST - %s/%s\SN_RE_VN_PP" %(username, password))

SSocket.Read()

SSocket.Close()