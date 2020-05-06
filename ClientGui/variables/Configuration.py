import os


class Configuration(object):

    #ip Address of Server
    ipAddress = "192.168.1.13"
    portNumber = 2003
    port_for_website = 2000

    Username = "User"

    log_path = os.getcwd() + "/Logging/logs/"

    frames = None
    quality = None

    gif_running = None

    # Timer
    start_time = None
    end_time = None

    stream_started = False
    connection = None
    Logstarted = False

    version = 1.1