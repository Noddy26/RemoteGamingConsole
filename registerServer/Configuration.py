
class Configuration(object):

    emailUserCount = None
    CannotConnect = None

    #ip Address of Server
    ipAddress = "192.168.0.13"
    portNumber = 3000

    # paths
    adduserdir = "/home/pi/WebServer/registerServer/UserToBeAdded/"
    userfilepath = adduserdir + "users.txt"

    templates = r"/home/pi/WebServer/registerServer/templates/"

    adminhtml = templates + "admin.html"
    adminhtmlbcakup = templates + "admin.html.bck"

    # admin details
    adminusername = "Administrator"
    adminpassword = "12shroot"

    # Sql Login details
    sqldatabase = "users"
    sqlusertable = "registeredusers"
    sqlhost = "localhost"
    sqluser = "root"
    sqlpassword = "12shroot"

    # Email of Admin
    AdminemailAddress = "neil.morrison89@gmail.com"
    GamingEmailAddress = "gamingserver.project@gmail.com"
    GamingEmailPassword = "GamingServer2019"
