import subprocess
import time

while True:
    subprocess.call("macchanger -a ens33", shell=True)#it will change mac add.
    time.sleep(3)# it will delay 3 sec.