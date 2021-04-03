#The Magicians
#FTP Covert Channel
#Last Update: 4/3/2021  1:40pm

from ftplib import FTP

### Golobal Constants ###

METHOD = 7 #METHOD should be 7 or 10

# FTP server details
IP = "138.47.102.120"
PORT = 21
USER = "anonymous"
PASSWORD = ""
FOLDER = "/7/"
USE_PASSIVE = True # set to False if the connection times out

### Functions ###

# display the folder contents and translate to binary
def stripMine():
    msg = ""
    for f in files:
        if METHOD == 7:
            vals = f[3:10]
        elif METHOD == 10:
           vals = f[:10]
        for v in vals:
            #skip files with character in the first 3 bits if method == 7
            if ((f[0:3] == "---") and (METHOD == 7)) or (METHOD == 10):
                if v == "-":
                    msg += "0"
                else:
                    msg += "1"
    return msg

#Decode the binary message and return an ASCII string
def decode(msg):
    #stores binary strings for each character
    binaryCharacters = []
    i = 0
    while(i < len(msg)):
        #breaks the main string of numbers into 7-bit segments
        binaryCharacters.append(msg[i:i+7])
        i+=7
    #translates binary to base 10
    base10Characters = []
    for b in binaryCharacters:
        base10Characters.append(int(b, 2))
    #translates base 10 to ASCII
    ASCIICharacters = ""
    for c in base10Characters:
        ASCIICharacters += chr(c)
    return ASCIICharacters

##############
###  Main  ###
##############

# connect and login to the FTP server
ftp = FTP()
ftp.connect(IP, PORT)
ftp.login(USER, PASSWORD)
ftp.set_pasv(USE_PASSIVE)

# navigate to the specified directory and list files
ftp.cwd(FOLDER)
files = []
ftp.dir(files.append)

# exit the FTP server
ftp.quit()


#Translate message
bin_msg = stripMine()
print(decode(bin_msg))
