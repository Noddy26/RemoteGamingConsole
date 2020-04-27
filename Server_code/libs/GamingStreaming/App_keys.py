class AppKeys(object):

    # keys to check from client
    controller_key = "_"
    Login_key = "+"
    StartStrem_key = "StartStreamingServer"
    ip_key = "`"
    StopStrem_key = "Stop"
    Terminate_key = "Connection Terminate"
    Version_key = "version"
    LogFile_key = "*****************Start of Log********************"
    enable_two_player = "Enable/twoPlayer"
    disable_two_player = "disable/twoPlayer"

    # keys to send to client Gui
    Gui_streamStared = "StreamStarted"
    Gui_Access = "Access Granted"
    Gui_denied = "Access Denied"
    Gui_Ip_Found = "IP Found in database"
    Gui_Ip_Not_Found = "No Ip Found in database"
    Gui_Enable_two_player = "Enable/twoPlayer"
    Gui_Disable_two_player = "disable/twoPlayer"
    Gui_Logout = "Logged out"
    Gui_send_ip = "send ip"

    # keys to send to client Android
    streamStared = "StreamStarted\n"
    Access = "Access Granted\n"
    denied = "Access Denied\n"
    Ip_Found = "IP Found in database\n"
    Ip_Not_Found = "No Ip Found in database\n"
    Enable_two_player = "Enable/twoPlayer\n"
    Disable_two_player = "disable/twoPlayer\n"
    Logout = "Logged out\n"

    # Sql
    AddIp = "UPDATE userdetails set ipAddress = '%s' WHERE username= '%s';"
    Loggedin = "UPDATE userdetails set login = 'True' WHERE username='%s';"
    GetUser = "SELECT username FROM userdetails Where ipAddress='%s';"
    Loggedout = "UPDATE userdetails set login = 'False' WHERE username='%s';"