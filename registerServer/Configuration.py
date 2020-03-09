
class Configuration(object):

    emailUserCount = None
    CannotConnect = None

    #ip Address of Server
    ipAddress = "192.168.1.13"
    portNumber = 2000
    server_running = None

    # paths
    adduserdir = "/home/pi/Server/registerServer/UserToBeAdded/"
    logDir = "/home/pi/Server/registerServer/GamingStreaming/User_logs/"
    userfilepath = adduserdir + "users.txt"

    templates = r"/home/pi/Server/registerServer/templates/"

    adminhtml = templates + "admin.html"
    adminhtmlbcakup = templates + "admin.html.bck"

    userhtml = templates + "Users.html"
    userhtmlbackup = templates + "Users.html.bck"

    # admin details
    adminusername = "Administrator"
    adminpassword = "12shroot"

    # Sql Login details
    sqldatabase = "users"
    sqlusertable = "userdetails"
    sqlhost = "localhost"
    sqluser = "root"
    sqlpassword = "12shroot"

    # Email of Admin
    AdminemailAddress = "neil.morrison89@gmail.com"
    GamingEmailAddress = "gamingserver.project@gmail.com"
    GamingEmailPassword = "GamingServer2019"

    # Gui Server Control
    #serverPath = "/root/IdeaProjects/GamingServer/out/production/GamingServer"
    #serverFile = "ServerForGui.Main"
    running = False

    CheckforemptyString = False
    Serverport = 2003

    # Streming control
    stream_portNumber = 2005
    streamStarted = False
    stream_socket = None
    streaming_has_started = False

    # Sockets
    Gui_Socket = None
    Stream_Socket = None

    # gpio
    pins_high = False
