# SN == Sugestao de Noticia---------------------------------
# RE == Report de Erro--------------------------------------
# VN == Votaçao de Noticia----------------------------------
# PP == Para Publicar---------------------------------------
#Made By: wi6n3l Profissional Contact: wi6n3lACVDS@gmail.com Discord: wi6n3l#7434
import SSocket

#Logins usernames and passwords list, in future a JSON
logins = {"wi6n3l":"f3e6beb3561e55e9d44be919129df23aef785e3ee39c66dbeb8136a9", "teste":"7e460ed4c46e68399bacc44972d7a3b7cff54abrec137765a151cdf8", "teste2":" 7e460ed4c46e68399bacc44972d7a3b7cff54ab37c137765a151cdfr"}
#Roles usernames and Role, in future another JSON
roles = {"Administrador":"wi6n3l", "Programador":"wi6n3l-teste1", "Publicador":"teste2-teste5", "Aprovador":"teste3-wi6n3l", "Perito":"teste4"}
#In Future new lists of Language and what is their expeciality

#Opening Server
SSocket.Server_wait(1000, 2312)
#I Like to let the while True changeble, with a True defined variable
rv = True

def sugestoes_de_noticias():
    with open("SN.data", "r") as file:
        snf = file
        return snf.read()

#print(sugestoes_de_noticias())

def report_de_erro():
    with open("RE.data", "r") as file:
        ref = file
        return ref.read()

#print(report_de_erro())

def votação_de_noticia(action, action2, index):
    if action == "votar":
        if action2 == "up":
            print("up")

        elif action2 == "down":
            print("down")



    with open("VN.data", "r") as file:
        vnf = file
        vnv = vnf.read()
        print(vnv)
        vns = vnv.split("\n")
        print(vns)

#votação_de_noticia()

def sugestoes_de_noticias():
    with open("SN.data", "r") as file:
        snf = file
        return snf.read()

#print(sugestoes_de_noticias())

# SN == Sugestao de Noticia---------------------------------
# RE == Report de Erro--------------------------------------
# VN == Votaçao de Noticia----------------------------------
# PP == Para Publicar---------------------------------------

#sugestoes_de_noticias()

#Mainloop
while rv:
    SSocket.Server_accept() #Acepting Server Connections
    print("acc") #Debuging (D)-----------------------------------
    a = SSocket.Read(10000) #Reciving socket messae from DBClient (information requests)
    print("a") #D------------------------------------------------
    if a.startswith("DB-REQUEST - "): #Verify that is the DBClient making a Db request
        print("if") #D-------------------------------------------
        #Formating the request
        s = a.index("/") + 1
        bs = a.index(r"\\"[1])
        print("bbs") #D------------------------------------------
        #Defining User and Pssword Hash inside the request
        user = a[13:s - 1]
        password = a[s:bs]
        print("up") #D--------------------------------------------
        if user in logins and logins[user] == hashlib.sha224(str(password).encode("utf-8")).hexdigest()password: #Verifing the username and Password coincide in DB
            c = a[bs + 1:] #Defining the "Final Request"
            print(c) #D
            d = c.split("_")
            administrador = roles["Administrador"].split("-")
            programador = roles["Programador"].split("-")
            publicador = roles["Publicador"].split("-")
            aprovador = roles["Aprovador"].split("-")
            perito = roles["Perito"].split("-")
            for request in d:
                if request == "SN" and user in aprovador:
                    print("SN")
                elif request == "RE" and user in programador:
                    print("RE")
                elif request == "VN" and user in perito:
                    print("VN")
                elif request == "PP" and user in publicador:
                    print("PP")
                else:
                    print("Não tem permissão para usar este comando, ou ele não existe!")

    elif a.startswith("APIREFRESH - "):
        print(a)