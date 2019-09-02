import os
import shutil
import time

def hourMin ():
    timeCal = time.localtime(time.time())
    timePrinteryr  = timeCal.tm_year
    timePrinterday = timeCal.tm_mday
    timePrinte
    rmon = timeCal.tm_mon
    print ("{}{}{}"
       .format(timePrinterday, timePrintermon, timePrinteryr)) 

def makeDir ():
    access_rights = 0o755
    path = "/tmp/dirtest"
    curr = path + str(hourMin)
try:
    os.mkdir(curr)
except OSError:
    print ("Creation of the directory %s failed" % curr)
else:
        print ("Successfully created the directory %s " % curr)
makeDir()