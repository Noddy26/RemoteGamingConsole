
class Configuration(object):

    emailUserCount = None
    CannotConnect = None

    # paths
    adduserdir = "UserToBeAdded//"
    userfilepath = adduserdir + "users.txt"

    templates = r"/home/neil/registerServer/templates/"

    adminhtml = templates + "admin.html"
    adminhtmlbcakup = templates + "admin.html.bck"

    # admin details
    adminusername = "Administrator"
    adminpassword = "12shroot"

    # Sql Login details
    sqldatabase = "users"
    sqlhost = "localhost"
    sqluser = "root"
    sqlpassword = "12shroot"
