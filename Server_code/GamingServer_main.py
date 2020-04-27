import os
from libs.Console.Terminal import Output
from ControlServer import app
from libs.Methods.FileMethods import FileMethods
from libs.Start_up.Startup import StartUp
from libs.variables.Configuration import Configuration


def main():
    if str(os.getcwd()).__contains__("GamingServer"):
        Configuration.aboslute_path = os.getcwd()
    else:
        Configuration.aboslute_path = str(os.getcwd()) + "/GamingServer"
    StartUp()
    FileMethods.returnHTMLpageBack(Configuration.adminhtml, Configuration.adminhtmlbcakup)
    app.secret_key = os.urandom(12)
    app.run(debug=True, host=Configuration.ipAddress, port=Configuration.portNumber)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        Output.red("Keyboard Error Occurred")
    except SystemExit:
        Output.red("SystemExit")
    except OSError as e:
        Output.red(e)
    except:
        Output.red("Unknown Error Caused Crash")
