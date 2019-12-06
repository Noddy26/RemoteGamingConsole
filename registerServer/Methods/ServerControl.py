import os
from Configuration import Configuration
import subprocess
import signal

class ServerControl:

    def __init__(self):
        print("Control Server")

    def turnOffServer(self):
        if Configuration.running is not None:
            print("turning off Server")
            print(Configuration.running.pid)
            os.killpg(Configuration.running.pid, signal.SIGTERM)
            Configuration.running = None
            return True
        else:
            return False

    def turnOnServer(self):
        if Configuration.running == None:
            print("turning on server")
            dirpath = os.getcwd()
            os.chdir(Configuration.serverPath)
            Configuration.running = subprocess.Popen("sudo /usr/bin/java " + Configuration.serverFile + " &",
                                                     shell=True, preexec_fn=os.setsid)
            os.chdir(dirpath)
            return True
        else:
            return False
