from Server_code.libs.FileFuctions.FilePaths import FilePaths
from Server_code.libs.variables.Configuration import Configuration


class ReadPaths():

    def __init__(self):

        Configuration.database_file = FilePaths.join_path(Configuration.aboslute_path,
                                                          "libs/Setup/ServerDetails.db")

        Configuration.setup_detail_file = FilePaths.join_path(Configuration.aboslute_path,
                                                              "libs/Setup/setup-parameters.yml")

        Configuration.adduserdir = FilePaths.join_path(Configuration.aboslute_path, "UserToBeAdded/")

        Configuration.logDir =FilePaths.join_path(Configuration.aboslute_path, "libs/GamingStreaming/User_logs/")

        Configuration.userfilepath = FilePaths.join_path(Configuration.adduserdir, "users.txt")

        Configuration.templates = FilePaths.join_path(Configuration.aboslute_path, "templates/")

        Configuration.adminhtml = FilePaths.join_path(Configuration.templates, "admin.html")

        Configuration.adminhtmlbcakup = FilePaths.join_path(Configuration.templates, "admin.html.bck")

        Configuration.userhtml = FilePaths.join_path(Configuration.templates, "Users.html")

        Configuration.userhtmlbackup = FilePaths.join_path(Configuration.templates, "Users.html.bck")
