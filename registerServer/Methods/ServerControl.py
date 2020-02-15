from ClientGui.Configuration import Configuration
from GamingStreaming.Server import Server


class ServerControl:

    def __init__(self):
        print("Control Server")
        self.threads = []

    def turnOffServer(self):
        if Configuration.running is not False:
            print("turning off Server")
            Server().stop()
            Configuration.running = False
            return True
        else:
            return False

    def turnOnServer(self):
        if Configuration.running is False:
            try:
                print("turning on server")
                newthread = Server()
                newthread.start()
                self.threads.append(newthread)
            except():
                for t in self.threads:
                    t.join()
            return True
        else:
            return False
