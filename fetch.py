#The Magicians
#FTP Covert Channel
#Last Update: 4/3/2021  12:30pm


from ftplib import FTP

def filtration():
    chars = [" ", "'", ".", ","]
    for i in range(26):
        chars.append(chr(i+65))
        chars.append(chr(i+97))
    return chars

# display the folder contents
def stripMine():
    msg = ""
    for f in files:
        if METHOD == 7:
            vals = f[3:10]
        elif METHOD == 10:
           vals = f[:10]
        for v in vals:
            if v == "-":
                msg += "0"
            else:
                msg += "1"
    return msg

def decode(bits, msg, valid_charset):
    #print(msg)
    l = len(msg)
    i = 0
    dec_msg = ""
    while i < l:
        if (l-i) < bits:
            span = l-i
        else:
            span = bits
        temp_char = chr(int(msg[i:(i+span)], 2))
        if temp_char in valid_charset:
            dec_msg += temp_char
        i += span
    return dec_msg

##############
###  Main  ###
##############

#First, get message from channel

METHOD = 7 #METHOD should be 7 or 10

# FTP server details
IP = "138.47.102.120"
PORT = 21
USER = "anonymous"
PASSWORD = ""
FOLDER = "/7/"
USE_PASSIVE = True # set to False if the connection times out

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
msg_chars = filtration()
bin_msg = stripMine()
print(decode(METHOD, bin_msg, msg_chars))
