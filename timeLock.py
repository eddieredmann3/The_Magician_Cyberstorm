from time import *
from sys import *
from hashlib import *

def time_differential(ep, curr):
    ep_t_struct = strp_time(ep, "%Y %m %d %H %M %S")
    
    encodedValue = md5(md5())

    
# we can find the epoch using the following commmand according to the time library documentation
epoch = ""
for line in stdin:
    if 'Exit' == line.rstrip():
        break
    epoch += line

#print(epoch)
# False for normal operation, True for debugging
debug = True

# When true, time will be set manually
if(debug == True):
    # MUST SET MANUAL VALUE WHEN USING DEBUG MODE
    curr_time = "2013 05 06 07 43 25"

# When false, time will use system time.
else:
    temp_time = localtime()
    curr_time = strftime("%Y %m %d %H %M %S", temp_time)
    print(curr_time)