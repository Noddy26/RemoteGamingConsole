import subprocess
import sys
import time
import requests
from ipython_genutils.py3compat import xrange
from libs.Console.Terminal import Output
from libs.Server_logging.Logging import Logger


class AutoUpgrade():

    def __init__(self):
        self.upgradble = False
        self.url = 'https://raw.githubusercontent.com/Noddy26/RemoteGamingConsole/master/Gaming_Server_change_log'
        num, log_list = self.checkgit()
        if num is not None and log_list is not None:
            self.askquestion(num, log_list)

    def checkgit(self):
        global num
        req = requests.get(self.url)
        content = req.content
        data = content.decode()
        list_data = data.split("\n")
        for each in list_data:
            if each.__contains__("Rpm version"):
                ver = each.split(":")
                num = float(ver[1])
                rpm = self.check_version()
                if num > rpm:
                    self.upgradble = True
        if self.upgradble is True:
            for each in list_data:
                if each.__contains__("*changes:"):
                    log_list = each.split(",")
                    return num, log_list
        return None, None

    def askquestion(self, ver, changelog):
        yes = ["yes", "Yes", "Y", "y"]
        no = ["no", "No", "N", "n"]
        Output.red("\r\nA higher version of the tool you are using has been detected.")
        Output.green("\r\nChangelog for Latest RPM")
        for each in changelog:
            Output.yellow("%s" % each.replace("*changes: ", "").replace(" ", ""))
        Output.white("\r\nWould you like to upgrade to the newest RPM")
        while True:
            userinput = input("Answer yes/no: ")
            if userinput in yes:
                self.upgrade(ver)
                break
            elif userinput in no:
                Logger.info("Upgrade skipped")
                break
            else:
                Output.red("Invalid Entry")

    def upgrade(self, ver):
        filename = "GamingServer-%s-PA1.noarch.rpm" % ver
        url = "https://raw.githubusercontent.com/Noddy26/RemoteGamingConsole/master/" + filename
        cmd = "wget --no-check-certificate --content-disposition " + url + " > /dev/null"
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout
        process.close()
        command = "sudo alien " + filename + " 2> /dev/null"
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout
        self.loadbar(60, "Getting RPM")
        process.close()
        debfile = "gamingserver_%s-1_all.deb" % ver
        upgrade = "dpkg --install " + debfile
        pro = subprocess.Popen(upgrade, shell=True, stdout=subprocess.PIPE).stdout
        self.loadbar(60, "Upgrading the package")
        pro.close()
        Output.green("The tool has been upgraded to the latest verson %s" % ver)
        Output.green("Run 'sudo python3 GamingServer_main.py' to run the tool")

    def loadbar(self, duration, message):
        print("\n")
        Output.yellow(message)
        sys.stdout.write("[%s]" % (" " * duration))
        sys.stdout.flush()
        sys.stdout.write("\b" * (duration + 1))
        for i in xrange(duration):
            time.sleep(0.4)
            sys.stdout.write("=")
            sys.stdout.flush()
        sys.stdout.write("]\n")


    def check_version(self):
        version_check_cmd = "dpkg -l gamingserver | egrep gamingserver"
        version_check = subprocess.Popen(version_check_cmd, shell=True, stdout=subprocess.PIPE).stdout
        check_status = version_check.read()
        version_check.close()
        version = str(check_status).split(" ")
        final_verson = str(version[5]).replace("-1", "")
        return float(final_verson)
