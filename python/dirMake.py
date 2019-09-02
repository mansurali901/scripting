import os
import shutil
import time
import json
import vars

def hourMin ():
    timeCal = time.localtime(time.time())
    print (timeCal)
    timePrinteryr  = timeCal.tm_year
    timePrinterday = timeCal.tm_mday
    timePrintermon = timeCal.tm_mon
    timePrinterhr = timeCal.tm_hour
    timePrintermin = timeCal.tm_min
    return ("{0}{1}{2}-{3}{4}" .format(timePrinterday, timePrintermon, timePrinteryr, timePrinterhr, timePrintermin)) 

def makeDir ():
    access_rights = 0o755
    path = "/tmp/dirtest/"
    curr = path + str(hourMin())
    
    try:
        os.mkdir(curr)
        
    except OSError:
        print ("Creation of the directory %s failed" % curr)
    else:
            print ("Successfully created the directory %s " % curr)
makeDir()