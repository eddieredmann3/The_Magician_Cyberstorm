from time import *
from sys import *
from hashlib import *

def time_differential(ep, curr):
    #makes the epoch time that we read from stdin a usable form
    ep_t_struct = strptime(ep, "%Y %m %d %H %M %S")
    
    #gets the seconds so that we only change the code once per minute
    ep_t_sec = ep_t_struct.tm_sec
    curr_t_sec = curr.tm_sec
    
    #makes the struct_times into floating point seconds since the true epoch
    ep_t = mktime(ep_t_struct)
    curr_t = mktime(curr)
    
    #sets the second offset so that we only change the code once per minute
    if curr_t_sec > ep_t_sec:
        sec_diff = curr_t_sec - ep_t_sec
    else:
        sec_diff = curr_t_sec + (60 - ep_t_sec)
    
    #returns the elapsed time
    return ((curr_t - ep_t) - sec_diff)
    
def hash_code_get(time_diff):
    time_diff = str(int(time_diff))
    
    #uses the hashlib md5 function to convert the elapsed time string to a hash
    temp_hash = md5(time_diff.encode())
    #then it actually turns it into a hexadecimal hash
    temp_hash = temp_hash.hexdigest()
    
    #repeating the process on the already hashed function
    hash_val = md5(temp_hash.encode())
    hash_val = hash_val.hexdigest()
    
    letterValue = 0
    letterString = ""
    numValue = len(hash_val) -1
    numString = ""
    letters = ["a", "b", "c", "d", "e", "f"]
    num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    intValue = 0
    while(letterValue < 2):
        if(hash_val[intValue] in letters):
            letterString += hash_val[intValue]
            letterValue += 1
            intValue += 1
        else:
            intValue += 1
    intValue = 0
    while(intValue < 2):
        if(hash_val[numValue] in num):
            numString += hash_val[numValue]
            numValue -= 1
            intValue += 1
        else:
            numValue -= 1
    
    #print(hash_val[len(hash_val)-1])
    #print(numString)
    code = letterString + numString
    #code = hash_val
    #code = hash_val[0:2] + hash_val[-2:]
    return code

# we can find the epoch using the following commmand according to the time library documentation
#epoch = ""
#for line in stdin:
#    #reads the epoch from the epoch file or stdin
#    if 'Exit' == line.rstrip():
#        break
#    epoch += line

epoch = input()

# False for normal operation, True for debugging
debug = True 

# When true, time will be set manually
if debug == True:
    curr_time = "2010 06 13 12 55 34"
    curr_time_s = strptime(curr_time,"%Y %m %d %H %M %S")
    #print(curr_time_s)
    t = time_differential(epoch, curr_time_s)
    #print(t)
    print(hash_code_get(t) + "\n")
    print("current system time: " + curr_time)

else:
    curr_time = localtime()
    curr_time_s = strftime("%Y %m %d %H %M %S", curr_time)
    #print(curr_time_s)
    t = time_differential(epoch, curr_time)
    print(hash_code_get(t) + "\n")
    print("current system time: " + curr_time_s)
