
class Configuration(object):

    emailUserCount = None
    CannotConnect = None

    #ip Address of Server
    ipAddress = None
    portNumber = 2000
    server_running = False

    # paths
    adduserdir = "/home/pi/GamingServer/Server_code/UserToBeAdded/"
    logDir = "/home/pi/GamingServer/Server_code/GamingStreaming/User_logs/"
    userfilepath = adduserdir + "users.txt"

    templates = r"/home/pi/GamingServer/Server_code/templates/"

    adminhtml = templates + "admin.html"
    adminhtmlbcakup = templates + "admin.html.bck"

    userhtml = templates + "Users.html"
    userhtmlbackup = templates + "Users.html.bck"

    # admin details
    adminusername = None
    adminpassword = None

    # Sql Login details
    sqldatabase = None
    sqlusertable = None
    sqlhost = None
    sqluser = None
    sqlpassword = None

    # Email of Admin
    AdminemailAddress = None
    GamingEmailAddress = None
    GamingEmailPassword = None

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

    # database file
    database_file = "ServerDetails.db"
    setup_detail_file = r"C:\Users\neilm\PycharmProjects\GamingGui\Server_code\Setup\setup-parameters.yml"#"/home/pi/GamingServer/Server_code/Setup/setup-parameters.yml"
    database_table = 'CREDENTIALS'
