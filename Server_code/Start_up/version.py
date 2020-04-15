import subprocess
from datetime import date

from Server_code.Console.Terminal import Output


class GetVersion():

    def __init__(self):
        year = date.today().strftime("%Y")
        version_check_cmd = "rpm -qi GaminServer | egrep \"^Version \" | awk -F ':' '{print $2}' | awk '{print $1}'"
        version_check = subprocess.Popen(version_check_cmd, shell=True, stdout=subprocess.PIPE).stdout
        check_status = version_check.read()
        version_check.close()
        if check_status != "" and check_status is not None:
            version_info = "\nGamingServer Service %s \nNeil Morrison %s - All rights reserved.\n"\
                           % (str(check_status).strip(), str(year))
            Output.white(version_info)

        else:
            Output.white("Version Could not be fetched")
