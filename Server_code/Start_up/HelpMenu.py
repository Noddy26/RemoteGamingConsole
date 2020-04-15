from Server_code.Console.Terminal import Output


class Help:

    def __init__(self):
        Output.white("-v\t--version\tdisplay version information")
        Output.white("-s\t--setup\tsets up the Server")
        Output.white("-h\t--help\tDisplays command line options")
