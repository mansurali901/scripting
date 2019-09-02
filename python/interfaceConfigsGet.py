import os
import subprocess
import shutil
import netifaces as ni 
from subprocess import check_output

ip = check_output(['hostname', '-I'])
print(ip)

# Copy File
newpath = shutil.copy('hosts.txt', '/tmp/')

# Get interface Info
ip = ni.ifaddresses('eth0')
print(ip)