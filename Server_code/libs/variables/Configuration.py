
class Configuration(object):

    aboslute_path = None
    emailUserCount = None
    CannotConnect = None

    #ip Address of Server
    ipAddress = None
    portNumber = 2000
    server_running = False

    # paths
    adduserdir = None
    logDir = None
    userfilepath = None

    templates = None

    adminhtml = None
    adminhtmlbcakup = None

    userhtml = None
    userhtmlbackup = None

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
    database_file = None
    setup_detail_file = None
    database_table = 'CREDENTIALS'

    # two player
    secondplayer = False
    versionGui = 1.1
    versionApp = 1.1
